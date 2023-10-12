#pragma once

#include <string>

/**
 * @struct Node
 * @brief Estrutura de nó para armazenar palavras em listas encadeadas
 */
struct Node {
  std::string word;      /**< A palavra armazenada no nó */
  Node *nextInBasicList; /**< Ponteiro para o próximo nó na lista básica */
  Node *crossListNext;   /**< Ponteiro para o próximo nó na 'lista 4' */

  Node(const std::string &word)
      : word(word), nextInBasicList(nullptr), crossListNext(nullptr) {}
};
