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
        if self.vazia():
            return 0
        soma: int = 0
        for i in range(self.nelements):
            soma += self.dados[i]
        return soma / self.nelements

    # d) Retorna a soma dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma(self) -> int:
        if self.vazia():
            return 0
        soma: int = 0
        for i in range(self.nelements):
            soma += self.dados[i]
        return soma

    # e) Retorne a soma dos quadrados dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma_dos_quadrados(self) -> int:
        if self.vazia():
            return 0
        soma: int = 0
        for i in range(self.nelements):
            soma += self.dados[i] ** 2
        return soma
