#include "LinkedList.hpp"

LinkedList::LinkedList() : head(nullptr) {}

LinkedList::~LinkedList() {
  while (this->head) {
    Node *tmp = this->head;
    this->head = this->head->next;
    delete tmp;
  }
}

void LinkedList::insert(const std::string &word) {
  Node *node = new Node(word);
  if (!this->head || word < this->head->word) {
    node->next = this->head;
    this->head = node;
    return;
  }

  Node *curr = this->head;
  while (curr->next) {
    if (word < curr->next->word) {
      node->next = curr->next;
      curr->next = node;
      return;
    }
    curr = curr->next;
  }

  curr->next = node;
}

bool LinkedList::find(const std::string &word) {
  Node *curr = this->head;
  while (curr) {
    if (curr->word.compare(word) == 0) {
      return true;
    }
    curr = curr->next4;
  }
  return false;
}
