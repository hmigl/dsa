class Lista:
    def __init__(self, maxnelemnts: int) -> None:
        self.maxnelemnts: int = maxnelemnts
        self.dados: list[int] = [0] * maxnelemnts
        self.nelements: int = 0

    def consulta(self, x: int) -> tuple[bool, int]:
        i: int = 0
        while i < self.nelements and self.dados[i] != x:
            i += 1
        return (True, i) if i < self.nelements else (False, -1)

    def insere(self, x: int) -> bool:
        if self.nelements == self.maxnelemnts or self.consulta(x) != (False, -1):
            return False
        self.dados[self.nelements] = x
        self.nelements += 1
        return True

    # insere(), mas sem a limitacao das chaves repetidas
    def insere_rep(self, x: int) -> bool:
        if self.nelements == self.maxnelemnts:
            return False
        self.dados[self.nelements] = x
        self.nelements += 1
        return True

    def remove(self, x: int) -> None:
        ta_na_lista, i = self.consulta(x)
        if not ta_na_lista:
            return
        self.nelements -= 1
        self.dados[i] = self.dados[self.nelements]

    def imprime(self) -> None:
        for i in range(self.nelements):
            print(self.dados[i])

    def vazia(self) -> bool:
        return self.nelements == 0

    # a) Retorne o menor elemento da lista. Se a lista nao tiver elementos,
    # a funcao deve retornar uma indicacao de que a lista esta vazia
    def min(self) -> tuple[int, bool]:
        if self.vazia():
            return (-1, False)

        min: int = self.dados[0]
        for i in range(1, self.nelements):
            if self.dados[i] < min:
                min = self.dados[i]

        return (min, True)

    # b) Retorne o numero de elementos com chave ımpar na lista
    def chaves_impares(self) -> int:
        chaves_impares: int = 0
        for i in range(self.nelements):
            if self.dados[i] % 2 != 0:
                chaves_impares += 1
        return chaves_impares

    # c) Retorne a media dos valores na lista. Se a lista estiver vazia, o valor da media deve
    # ser considerado como sendo zero.
    def media(self) -> float:
        soma: int = 0
        for i in range(self.nelements):
            soma += self.dados[i]
        return soma / self.nelements

    # d) Retorna a soma dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma(self) -> int:
        soma: int = 0
        for i in range(self.nelements):
            soma += self.dados[i]
        return soma

    # e) Retorne a soma dos quadrados dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma_dos_quadrados(self) -> int:
        soma: int = 0
        for i in range(self.nelements):
            soma += self.dados[i] ** 2
        return soma

    # (f) Elimine o k-esimo elemento da lista, se houver.
    # Considere que o primeiro elemento da lista esta na posicao 1
    def remove_k(self, k: int) -> bool:
        if k <= 0 or k > self.nelements or self.vazia():
            return False
        self.nelements -= 1
        self.dados[k - 1] = self.dados[self.nelements]
        return True

    # (g) Retire o elemento de maior valor da lista
    def remove_max(self) -> None:
        max, i = self.dados[0], 0
        for j in range(1, self.nelements):
            if self.dados[j] > max:
                max, i = self.dados[j], j
        self.nelements -= 1
        self.dados[i] = self.dados[self.nelements]

    # (h) Retire todos os elementos da lista com chave igual a um valor x, passado como parametro.
    # Para esta questao, considere que a lista pode conter mais de um elemento com mesmo valor de chave.
    def remove_todos_x(self, x: int) -> None:
        j: int = 0
        for i in range(self.nelements):
            if self.dados[i] != x:
                self.dados[j] = self.dados[i]
                j += 1
        self.nelements = j

    # (i) Reorganize a lista de forma que os elementos com chaves pares fiquem antes de elementos com chaves impares.
    def reorganiza_pares_antes(self) -> None:
        ultimo_par: int = 0
        for i in range(self.nelements):
            if self.dados[i] % 2 == 0:
                self.dados[ultimo_par], self.dados[i] = (
                    self.dados[i],
                    self.dados[ultimo_par],
                )
                ultimo_par += 1

    # (j) Modifique a lista de tal forma que todo elemento da lista com chave maior do que k venha antes
    # dos elementos na lista com chaves menores ou iguais a k.
    # O valor de k deve ser passado como parametro para a funcao.
    #
    # Em cada grupo de elementos - maiores do que k e menores ou iguais a k) -
    # a funcao deve manter a ordem original relativa dos elementos.
    def reorganiza_maiores_que_k_antes(self, k: int) -> None:
        res: list[int] = self.dados[:]
        j: int = 0
        for i in range(self.nelements):
            if self.dados[i] > k:
                res[j] = self.dados[i]
                j += 1
        for i in range(self.nelements):
            if self.dados[i] <= k:
                res[j] = self.dados[i]
                j += 1
        self.dados = res

    # (k) Inverta os elementos da lista
    def inverte_elementos(self) -> None:
        i: int = 0
        while i < self.nelements // 2:
            j: int = (self.nelements - 1) - i
            self.dados[i], self.dados[j] = self.dados[j], self.dados[i]
            i += 1

