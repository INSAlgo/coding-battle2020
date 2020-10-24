// Solution by Louis Sugy

#include <iostream>
#include <string>

int score(std::string& name) {
  const int l = name.size();
  bool bonus = false;

  int nv = 0;
#pragma omp parallel for reduction(+ : nv) schedule(guided)
  for (int i = 0; i < l; i++) {
    char c = name[i];
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y')
      nv++;
  }
  int s = 3 * nv - l;

#pragma omp parallel for reduction(|| : bonus) schedule(guided)
  for (int i = 0; i < l; i++) {
    bonus = bonus || (i < l - 2 && name[i] == 'k' &&
                      name[i + 1] == 'e' && name[i + 2] == 'r');
  }

  if (bonus)
    s += 5;

  if (s > 0) {
    bool palindrome = true;
#pragma omp parallel for reduction(&& : palindrome) schedule(guided)
    for (int i = 0; i < l / 2; i++) {
      palindrome = palindrome && name[i] == name[l - 1 - i];
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