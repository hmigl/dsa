#include "LinkedList.hpp"

LinkedList::LinkedList() : head(nullptr) {}

LinkedList::~LinkedList() {}

void LinkedList::insert(Node *node, Node *Node::*next) {
  std::string word = node->word;
  if (!this->head || word.compare(this->head->word) < 0) {
    node->*next = this->head;
    this->head = node;
    return;
  }

  Node *curr = this->head;
  while (curr->*next) {
    if (word.compare((curr->*next)->word) < 0) {
      node->*next = curr->*next;
      curr->*next = node;
      return;
    }
    curr = curr->*next;
  }

  curr->*next = node;
}

bool LinkedList::find(const std::string &word, Node *Node::*next) const {
  Node *curr = this->head;
  while (curr) {
    if (curr->word.compare(word) == 0) {
      return true;
    }
    curr = curr->*next;
  }
  return false;
}

void LinkedList::display(Node *Node::*next) const {
  Node *curr = this->head;

  if (!curr) {
    std::cout << "lista vazia\n";
    return;
  }

  while (curr) {
    std::cout << curr->word << '\n';
    curr = curr->*next;
  }
}

void LinkedList::clear(Node *Node::*next) {
  while (this->head) {
    Node *tmp = this->head;
    this->head = (this->head)->*next;
    delete tmp;
  }
}

void LinkedList::displayByLength(size_t n, Node *Node::*next) const {
  Node *curr = this->head;
  int i = 0;

  while (curr) {
    if (curr->word.length() == n) {
      std::cout << curr->word << '\n';
      ++i;
    }
    curr = curr->*next;
  }

  if (i == 0) {
    std::cout << "lista vazia\n";
  }
}

void LinkedList::displayAlphabetically(char from, char untill,
                                       Node *Node::*next) const {
  Node *curr = this->head;
  int i = 0;

  while (curr) {
    std::string word = curr->word;
    if (word.at(0) >= from && word.at(0) <= untill) {
      std::cout << curr->word << '\n';
      ++i;
    }
    curr = curr->*next;
  }

  if (i == 0) {
    std::cout << "lista vazia\n";
  }
}

Node *LinkedList::removeNode(const std::string &word, Node *Node::*next) {
  if (!this->head) {
    return nullptr;
  }

  if (this->head->word.compare(word) == 0) {
    Node *head = this->head;
    this->head = this->head->*next;
    return head;
  }

  Node *curr = this->head;
  while (curr->*next) {
    if ((curr->*next)->word.compare(word) == 0) {
      Node *tmp = curr->*next;
      curr->*next = (curr->*next)->*next;
      return tmp;
    }
    curr = curr->*next;
  }
  return nullptr;
}
