#include "CommandHandler.hpp"

CommandHandler::CommandHandler() {}

CommandHandler::CommandHandler(LinkedList list1, LinkedList list2,
                               LinkedList list3, LinkedList list4)
    : list1(list1), list2(list2), list3(list3), list4(list4) {}

CommandHandler::~CommandHandler() {}

void CommandHandler::insertWord() {
  std::string word;
  std::cin >> word;

  if (list4.find(word, &Node::next4)) {
    std::cout << "palavra ja existente\n";
    return;
  }

  list4.insert(word, &Node::next4);
  std::string::size_type size = word.length();
  if (size <= 5) {
    this->list1.insert(word, &Node::next);
    std::cout << "inseriu na 1\n";
  } else if (size >= 6 && size <= 10) {
    this->list2.insert(word, &Node::next);
    std::cout << "inseriu na 2\n";
  } else {
    this->list3.insert(word, &Node::next);
    std::cout << "inseriu na 3\n";
  }
}

void CommandHandler::listWords() {}

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
