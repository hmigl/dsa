#include "CommandHandler.hpp"

CommandHandler::CommandHandler() {}

CommandHandler::CommandHandler(LinkedList list1, LinkedList list2,
                               LinkedList list3, LinkedList list4)
    : list1(list1), list2(list2), list3(list3), list4(list4) {}

CommandHandler::~CommandHandler() {}

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
  std::cout << "palavra inserida: " << word << '\n';

  this->list4.insert(node, &Node::next4);
}

void CommandHandler::listWords() {
  int n;
  std::cin >> n;

  if (std::cin.fail()) {
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

void CommandHandler::listWordsByLength() {}

void CommandHandler::listWordsAlphabetically() {}

void CommandHandler::removeWord() {}

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
}
