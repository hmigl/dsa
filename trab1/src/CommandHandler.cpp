#include "CommandHandler.hpp"

#include "LinkedList.hpp"

CommandHandler::CommandHandler() {}

CommandHandler::CommandHandler(LinkedList list1, LinkedList list2,
                               LinkedList list3, LinkedList list4)
    : list1(list1), list2(list2), list3(list3), list4(list4) {}

CommandHandler::~CommandHandler() {}

void CommandHandler::run() {
  std::string command;

  for (;;) {
    std::getline(std::cin >> std::ws, command);

    if (command.compare("e") == 0) {
      std::cout << "gottem\n";
      break;
    } else if (command.compare("i") == 0) {
      std::cout << "gottim\n";
    } else if (command.compare("l") == 0) {
      std::cout << "gottlm\n";
    } else if (command.compare("x") == 0) {
      std::cout << "gottxm\n";
    } else if (command.compare("o") == 0) {
      std::cout << "gottom\n";
    } else if (command.compare("r") == 0) {
      std::cout << "gottrm\n";
    }
  }
}
