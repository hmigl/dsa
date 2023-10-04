#pragma once

#include <iostream>

#include "Node.hpp"

class LinkedList {
 public:
  LinkedList();
  LinkedList &operator=(const LinkedList &) = default;
  ~LinkedList();

  Node *head;

  void insert(Node *, Node *Node::*);
  bool find(const std::string &, Node *Node::*);
};
