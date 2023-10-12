#pragma once

#include <iostream>

#include "Node.hpp"

class LinkedList {
 public:
  LinkedList();
  LinkedList &operator=(const LinkedList &) = default;
  ~LinkedList();

  /**
   * @brief Insere um nó na lista encadeada de forma ordenada.
   *
   * @param node O nó a ser inserido na lista.
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   */
  void insert(Node *node, Node *Node::*next);

  /**
   * @brief Verifica a existência de uma palavra na lista encadeada.
   *
   * @param word A palavra a ser encontrada na lista.
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   *
   * @return true se a palavra foi encontrada na lista, false caso contrário.
   */
  bool find(const std::string &word, Node *Node::*next) const;

  /**
   * @brief Mostra todas as palavras armazenadas na lista, uma por linha.
   *
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   */
  void display(Node *Node::*next) const;

  /**
   * @brief Limpa uma lista, desalocando seus nós.
   *
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   */
  void clear(Node *Node::*next);

  /**
   * @brief Mostra as palavras da listas que possuam um tamanho \p size.
   *
   * @param size Tamanho da palavra.
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   */
  void displayByLength(size_t size, Node *Node::*next) const;

  /**
   * @brief Mostra as palavras que estejam entre \p from e \p untill (ambos
   * inclusos).
   *
   * @param from Limite inferior do intervalo.
   * @param untill Limite superior do intervalo.
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   */
  void displayAlphabetically(char from, char untill, Node *Node::*next) const;

  /**
   * @brief Remove, de uma lista, o nó que contém \p word.
   *
   * @param word Palavra visada.
   * @param next Um ponteiro para um membro da estrutura `Node` que indica a
   * próxima ligação na lista.
   * @return O nó a ser removido. Caso a palavra não esteja presente, nullptr.
   */
  Node *removeNode(const std::string &word, Node *Node::*next);

 private:
  Node *head;
};
