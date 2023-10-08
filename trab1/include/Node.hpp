#pragma once

#include <string>

struct Node {
  std::string word;
  Node *next;
  Node *next4;

  Node(const std::string &word) : word(word), next(nullptr), next4(nullptr) {}
};
