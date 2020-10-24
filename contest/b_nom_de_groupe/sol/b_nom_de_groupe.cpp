// Solution by Louis Sugy

#include <iostream>
#include <string>

int score(std::string name) {
  int l = name.size();
  bool bonus = false;
  const char *name_array = name.c_str();

  int nv = 0, nc = 0;
#pragma omp parallel for reduction(+ : nv, nc) schedule(guided)
  for (int i = 0; i < l; i++) {
    char c = name_array[i];
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y')
      nv++;
    else
      nc++;
  }
  int s = 2 * nv - nc;

#pragma omp parallel for reduction(|| : bonus) schedule(guided)
  for (int i = 0; i < l; i++) {
    bonus = bonus || (i < l - 2 && name_array[i] == 'k' &&
                      name_array[i + 1] == 'e' && name_array[i + 2] == 'r');
  }

  if (bonus)
    s += 5;

  if (s > 0) {
    bool palindrome = true;
#pragma omp parallel for reduction(&& : palindrome) schedule(guided)
    for (int i = 0; i < l / 2; i++) {
      palindrome = palindrome && name_array[i] == name_array[l - 1 - i];
    }
    if (palindrome)
      s *= 2;
  }

  return s;
}

int main(int argc, char **argv) {
  std::string name;
  std::cin >> name;
  std::cout << score(name) << std::endl;
  return 0;
}