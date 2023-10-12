#pragma once

#include <iostream>

#include "LinkedList.hpp"

class CommandHandler {
 public:
  CommandHandler(LinkedList, LinkedList, LinkedList, LinkedList);
  CommandHandler &operator=(const CommandHandler &) = default;
  ~CommandHandler();

  /**
   * @brief Executa o loop principal para processar comandos.
   *
   * Inicia um loop infinito que aguarda comandos do usuário. Os comandos
   * aceitos incluem 'i' para inserir uma palavra, 'l' para listar palavras, 'x'
   * para listar palavras por comprimento, 'o' para listar palavras em ordem
   * alfabética e 'r' para remover uma palavra. O comando 'e' encerra o loop e
   * finaliza a execução.
   */
  void run();

 private:
  CommandHandler();

  LinkedList list1, list2, list3, list4;

  /**
   * @brief Insere uma palavra na lista de acordo com seu tamanho
   */
  void insertWord();

  /**
   * @brief Lista palavras da lista selecionada com base na entrada do usuário.
   *
   * Um número (1, 2, 3 ou 4) deve ser fornecido para escolher a lista desejada.
   * Em seguida, a função exibirá as palavras da lista selecionada
   */
  void listWords() const;

  /**
   * @brief Lista palavras das listas com um comprimento específico em ordem
   * alfabética.
   *
   * As palavras são apresentadas na saída padrão, uma por linha, em ordem
   * alfabética. Caso não haja palavras com o número de letras dado, a saída é
   * 'lista vazia'
   */
  void listWordsByLength();

  /**
   * @brief Lista palavras em ordem alfabética de acordo com um intervalo de
   * caracteres.
   *
   * A função exibirá na saída padrão (stdout) as palavras que começam com
   * caracteres dentro desse intervalo, uma por linha. Caso não haja palavras
   * neste intervalo, a saída é 'lista vazia'
   */
  void listWordsAlphabetically() const;

  /**
   * @brief Remove uma palavra das listas.
   *
   * A palavra é lida da entrada padrão e é então verificado se ela existe na
   * lista. Se a palavra não existir, uma mensagem de erro é exibida. Caso
   * contrário, a palavra é removida das listas apropriadas
   */
  void removeWord();

  /**
   * @brief Obtém a lista apropriada com base no tamanho da palavra.
   *
   * @param size O tamanho da palavra para a qual a lista deve ser determinada.
   * @return Um ponteiro para a lista apropriada (1, 2 ou 3)
   */
  LinkedList *getListByWordSize(const std::string::size_type &);
};
