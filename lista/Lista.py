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
