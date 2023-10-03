#pragma once

#include "Node.hpp"

class LinkedList {
 public:
  LinkedList();
  LinkedList &operator=(const LinkedList &) = default;
  ~LinkedList();

  Node *head;

  void insert(const std::string &);
  bool find(const std::string &);
};
