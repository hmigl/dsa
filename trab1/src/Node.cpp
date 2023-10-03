#include "Node.hpp"

Node::Node() : word(), next(nullptr) {}

Node::Node(const std::string &word)
    : word(word), next(nullptr), next4(nullptr) {}

Node::Node(const Node &other) { *this = other; }

Node::~Node() {}
