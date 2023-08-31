class Lista:
    def __init__(self, maxnelemnts: int) -> None:
        self.maxnelemnts = maxnelemnts
        self.dados = [0] * maxnelemnts
        self.nelements = 0

    def consulta(self, x: int) -> bool:
        i: int = 0
        while i < self.nelements and self.dados[i] != x:
            i += 1
        return i < self.nelements

    def insere(self, x: int) -> bool:
        if self.nelements == self.maxnelemnts or self.consulta(x):
            return False
        self.dados[self.nelements] = x
        self.nelements += 1
        return True

    def remove(self, x: int) -> None:
        i: int = 0
        achou: bool = False
        while i < self.nelements - 1:
            if self.dados[i] == x:
                achou = True
                self.dados[i] = self.dados[i + 1]
                x = self.dados[i + 1]
            i += 1
        if self.nelements > 0 and (achou or self.dados[i] == x):
            self.nelements -= 1

    def imprime(self) -> None:
        for i in range(self.nelements):
            print(self.dados[i])
