#pragma once

#include <string>

class Node {
 public:
  Node();
  Node(const std::string &);
  Node(const Node &);
  Node &operator=(const Node &) = default;
  ~Node();

  std::string word;
  Node *next;
  Node *next4;
};
