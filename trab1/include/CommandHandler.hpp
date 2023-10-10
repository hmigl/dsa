#pragma once

#include <iostream>

#include "LinkedList.hpp"

class CommandHandler {
 public:
  CommandHandler(LinkedList, LinkedList, LinkedList, LinkedList);
  CommandHandler &operator=(const CommandHandler &) = default;
  ~CommandHandler();

  void run();

 private:
  CommandHandler();

  LinkedList list1, list2, list3, list4;

  void insertWord();
  void listWords() const;
  void listWordsByLength();
  void listWordsAlphabetically() const;
  void removeWord();
  LinkedList *getListByWordSize(const std::string::size_type &);
};
