#include "CommandHandler.hpp"

CommandHandler::CommandHandler() {}

CommandHandler::CommandHandler(LinkedList list1, LinkedList list2,
                               LinkedList list3, LinkedList list4)
    : list1(list1), list2(list2), list3(list3), list4(list4) {}

CommandHandler::~CommandHandler() {}

// Private methods implementation
// ----------------------------

LinkedList *CommandHandler::getListByWordSize(
    const std::string::size_type &size) {
  if (size <= 5) {
    return &this->list1;
  } else if (size <= 10) {
    return &this->list2;
  }
  return &this->list3;
}

void CommandHandler::insertWord() {
  std::string word;
  std::cin >> word;

  std::string::size_type size = word.length();
  LinkedList *list = getListByWordSize(size);

  if (list->find(word, &Node::next)) {
    std::cout << "palavra ja existente: " << word << '\n';
    return;
  }

  Node *node = new Node(word);
  list->insert(node, &Node::next);
  this->list4.insert(node, &Node::next4);
  std::cout << "palavra inserida: " << word << '\n';
}

void CommandHandler::listWords() const {
  int n;
  std::cin >> n;

  if (std::cin.fail()) {
    std::cin.clear();
    return;
  }

  switch (n) {
    case 1:
      this->list1.display(&Node::next);
      break;
    case 2:
      this->list2.display(&Node::next);
      break;
    case 3:
      this->list3.display(&Node::next);
      break;
    case 4:
      this->list4.display(&Node::next4);
      break;
    default:
      break;
  }
}

void CommandHandler::listWordsByLength() {
  size_t n;
  std::cin >> n;

  if (std::cin.fail()) {
    std::cin.clear();
    return;
  }

  LinkedList *list = getListByWordSize(n);
  list->displayByLength(n, &Node::next);
}

void CommandHandler::listWordsAlphabetically() const {
  char from;
  std::cin >> from;
  if (std::cin.fail()) {
    std::cin.clear();
    return;
  }

  char untill;
  std::cin >> untill;
  if (std::cin.fail()) {
    std::cin.clear();
    return;
  }

  this->list4.displayAlphabetically(from, untill, &Node::next4);
}

void CommandHandler::removeWord() {
  std::string word;
  std::cin >> word;

  LinkedList *list = getListByWordSize(word.size());
  if (!list->find(word, &Node::next)) {
    std::cout << "palavra inexistente: " << word << '\n';
    return;
  }

  list->removeNode(word, &Node::next);
  Node *removed = this->list4.removeNode(word, &Node::next4);
  delete removed;
  std::cout << "palavra removida: " << word << '\n';
}

// Public methods implementation
// ----------------------------

void CommandHandler::run() {
  std::string command;

  for (;;) {
    std::cin >> command;

    if (command.compare("e") == 0) {
      break;
    } else if (command.compare("i") == 0) {
      insertWord();
    } else if (command.compare("l") == 0) {
      listWords();
    } else if (command.compare("x") == 0) {
      listWordsByLength();
    } else if (command.compare("o") == 0) {
      listWordsAlphabetically();
    } else if (command.compare("r") == 0) {
      removeWord();
    }
  }
  this->list4.clear(&Node::next4);
}
