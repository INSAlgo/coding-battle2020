groupName = IO.read(:stdio, :line) |> String.trim()

nbVowels = Enum.count(String.codepoints(groupName), fn c -> c =~ ~r/[aeiouy]/ end)
nbConsonants = String.length(groupName) - nbVowels

score = 2 * nbVowels - nbConsonants
score = score + if String.contains?(groupName, "ker"), do: 5, else: 0
score = score * if score > 0 && groupName == String.reverse(groupName), do: 2, else: 1

IO.puts(score)
