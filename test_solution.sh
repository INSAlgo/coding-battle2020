#!/usr/bin/env bash

set -euo pipefail

################################################################################
## Input variables

SOURCE_CODE_PATH=$1

################################################################################
## Prints script usage.

usage() {
    echo "$0 [path_to_solution_source_code_to_test]"
    echo ""
    echo "Supported languages:"
    echo " - "
}

################################################################################
## Returns the file extension from the given full path.

get_extension() {
    FILE_PATH=$1
    FILE_NAME=$(basename "${FILE_PATH}")
    EXTENSION="${FILE_NAME##*.}"
    echo "${EXTENSION}"
}

################################################################################
## Count the number of input/output for the given problem

count_test_cases() {
    PROBLEM_BASE_DIR=$1
    NB_INPUTS=$(find "${PROBLEM_BASE_DIR}/input" -maxdepth 1 -type f | wc -l)
    NB_OUTPUTS=$(find "${PROBLEM_BASE_DIR}/output" -maxdepth 1 -type f | wc -l)
    if [ "${NB_INPUTS}" != "${NB_OUTPUTS}" ]; then
        echo "Error: there are a different number of inputs and outputs in '${PROBLEM_BASE_DIR}'."
        exit 1
    fi
    echo "${NB_INPUTS}"
}

################################################################################
## Creates a new temp directory.

get_new_temp_dir() {
    TEMP_DIR=$(mktemp -d -p '/tmp' 'codingbattle-XXXXXX')
    if [ ! -d "${TEMP_DIR}" ]; then
        echo "Failed to create a new temporary directory."
        exit 1
    fi
    echo "${TEMP_DIR}"
}

################################################################################
## Script entrypoint

if [ -z "${SOURCE_CODE_PATH}" ]; then
    echo "Missing path to solution source code to test."
    usage
    exit 1
fi

PROBLEM_BASE_DIR="$(dirname "${SOURCE_CODE_PATH}")/.."
INPUT_DIR="${PROBLEM_BASE_DIR}/input"
OUTPUT_DIR="${PROBLEM_BASE_DIR}/output"

if [ ! -d "${PROBLEM_BASE_DIR}" ] || [ ! -d "${INPUT_DIR}" ] || [ ! -d "${OUTPUT_DIR}" ]; then
    echo "Failed to detect path to the problem, please check the given file path."
    exit 1
fi

echo "Testing solution: ${SOURCE_CODE_PATH}"

EXTENSION=$(get_extension "${SOURCE_CODE_PATH}")
case "${EXTENSION}" in
    py|py3)
        echo "Detected Python 3."
        which python3 || { echo "Python 3 is not installed."; exit 1; }
        COMMAND_LINE="python3 ${SOURCE_CODE_PATH}"
        ;;
    py2)
        echo "Detected Python 2."
        which python2 || { echo "Python 2 is not installed."; exit 1; }
        COMMAND_LINE="python2 ${SOURCE_CODE_PATH}"
        ;;
    c|cpp|rs|hs)
        if [ "${EXTENSION}" = "c" ]; then
            LANGUAGE="C"
            COMPILER="gcc"
            COMPILER_FLAGS=(-O2)
        fi
        if [ "${EXTENSION}" = "cpp" ]; then
            LANGUAGE="C++"
            COMPILER="g++"
            COMPILER_FLAGS=(-O2)
        fi
        if [ "${EXTENSION}" = "rs" ]; then
            LANGUAGE="Rust"
            COMPILER="rustc"
            COMPILER_FLAGS=(-O -C target-cpu=native)
        fi
        if [ "${EXTENSION}" = "hs" ]; then
            LANGUAGE="Haskell"
            COMPILER="ghc"
            COMPILER_FLAGS=(-no-keep-hi-files -no-keep-o-files)
        fi
        echo "Detected ${LANGUAGE}."

        TEMP_DIR=$(get_new_temp_dir) || exit 2
        BINARY="${TEMP_DIR}/$(basename "${SOURCE_CODE_PATH}").compiled"

        which ${COMPILER} || { echo "${COMPILER} is not installed."; exit 1; }

        if ! ${COMPILER} "${COMPILER_FLAGS[@]}" "${SOURCE_CODE_PATH}" -o "${BINARY}"; then
            echo "Failed to compile: ${SOURCE_CODE_PATH}"
            exit 1
        fi
        echo "Compiled ${LANGUAGE} code to: ${BINARY}"

        COMMAND_LINE="${BINARY}"
        ;;
    java)
        echo "Detected Java."

        TEMP_DIR=$(get_new_temp_dir) || exit 2

        if ! javac -d "${TEMP_DIR}" "${SOURCE_CODE_PATH}"; then
            echo "Failed to compile: ${SOURCE_CODE_PATH}"
            exit 1
        fi
        echo "Compiled Java code in: ${TEMP_DIR}"

        COMMAND_LINE="java -cp ${TEMP_DIR} $(basename "${SOURCE_CODE_PATH}" .java)"
        ;;
    exs)
        echo "Detected Elixir script."
        which elixir || { echo "Elixir is not installed."; exit 1; }
        COMMAND_LINE="elixir ${SOURCE_CODE_PATH}"
        ;;
    groovy)
        echo "Detected Groovy."
        which groovy || { echo "Groovy is not installed."; exit 1; }
        COMMAND_LINE="groovy ${SOURCE_CODE_PATH}"
        ;;
    *)
        echo "Unhandled language: ${EXTENSION}. Contributions are welcome!"
        exit 1
esac

NB_TEST_CASES=$(count_test_cases "${PROBLEM_BASE_DIR}")
MAX_TEST_CASE_NB=$((NB_TEST_CASES - 1))
FAILED="false"
for ((i = 0; i < MAX_TEST_CASE_NB; i++)); do
    echo "Testing $i"
    if ! diff --ignore-trailing-space <(${COMMAND_LINE} < "${INPUT_DIR}/input${i}.txt") "${OUTPUT_DIR}/output${i}.txt"; then
        FAILED="true"
    fi
done

if [ "${FAILED}" = "false" ]; then
    echo "Solution is correct."
else
    echo "Solution is invalid: ${SOURCE_CODE_PATH}"
    exit 1
fi
