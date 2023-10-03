#include "LinkedList.hpp"

LinkedList::LinkedList() : head(nullptr) {}

LinkedList::~LinkedList() {
  while (this->head) {
    Node *tmp = this->head;
    this->head = this->head->next;
    delete tmp;
  }
}

void LinkedList::insert(const std::string &word) {}
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
