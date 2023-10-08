#pragma once

#include <iostream>

#include "Node.hpp"

class LinkedList {
 public:
  LinkedList();
  LinkedList &operator=(const LinkedList &) = default;
  ~LinkedList();

  void insert(Node *, Node *Node::*);
  bool find(const std::string &, Node *Node::*) const;
  void display(Node *Node::*) const;
  void clear(Node *Node::*);
  void displayByLength(size_t, Node *Node::*) const;
  void displayAlphabetically(char, char, Node *Node::*) const;
  Node *removeNode(const std::string &, Node *Node::*);

 private:
  Node *head;
};
