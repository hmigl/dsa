#include "CommandHandler.hpp"
#include "LinkedList.hpp"

int main(void) {
  LinkedList list1, list2, list3, list4;

  CommandHandler handler(list1, list2, list3, list4);
  handler.run();
  return 0;
}
