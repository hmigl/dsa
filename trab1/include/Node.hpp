#pragma once

#include <string>

struct Node {
  std::string word;
  Node *nextInBasicList;
  Node *crossListNext;

  Node(const std::string &word)
      : word(word), nextInBasicList(nullptr), crossListNext(nullptr) {}
};
