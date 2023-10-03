#include "Node.hpp"

Node::Node() : word(), next(nullptr) {}

Node::Node(const std::string &word) : word(word), next(nullptr) {}

Node::Node(const Node &other) { *this = other; }

// Node &Node::operator=(const Node &other) {
//   if (this != &other) {
//     this->word = other.word;
//     this->next = other.next;
//   }
//   return *this;
// }

Node::~Node() {}
