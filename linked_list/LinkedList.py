class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def search(self, x: int) -> Node | None:
        curr: Node | None = self.head
        while (curr is not None) and (curr.key != x):
            curr = curr.next
        return curr

    def insert_back(self, x: int) -> bool:
        # if self.search(x):
        #     return False
        new: Node = Node(x)
        if self.is_empty():
            self.head = new
        else:
            curr: Node = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new
        return True

    def insert_front(self, x: int) -> bool:
        # if self.search(x):
        #     return False
        new: Node = Node(x)
        new.next = self.head
        self.head = new
        return True

    def remove(self, x: int) -> None:
        if not self.head:
            return
        if self.head.key == x:
            self.head = self.head.next
            return
        curr: Node = self.head
        while curr.next is not None:
            if curr.next.key == x:
                curr.next = curr.next.next
                return
            curr = curr.next

    def rem(self, x: int) -> None:
        node: Node | None = self.search(x)
        if node:
            node.key = self.head.key
            self.head = self.head.next

    def print(self) -> None:
        curr: Node | None = self.head
        while curr is not None:
            print(curr.key)
            curr = curr.next

    # a) Retorne o menor elemento da lista. Se a lista nao tiver elementos,
    # a funcao deve retornar uma indicacao de que a lista esta vazia
    def min(self) -> tuple[bool, int]:
        if self.is_empty():
            return (False, -1)
        curr, min = self.head, self.head.key
        while curr:
            k: int = curr.key
            if k < min:
                min = k
            curr = curr.next
        return (True, min)

    # b) Retorne o numero de elementos com chave ımpar na lista
    def chaves_impares(self) -> int:
        n: int = 0
        curr: Node | None = self.head
        while curr:
            if curr.key % 2 != 0:
                n += 1
            curr = curr.next
        return n

    # c) Retorne a media dos valores na lista. Se a lista estiver vazia, o valor da media deve
    # ser considerado como sendo zero.
    def media(self) -> float:
        sum = i = 0
        curr: Node | None = self.head
        while curr:
            sum += curr.key
            i += 1
            curr = curr.next
        return sum / i if i > 0 else 0

    # d) Retorna a soma dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma(self) -> int:
        sum: int = 0
        curr: Node | None = self.head
        while curr:
            sum += curr.key
            curr = curr.next
        return sum

    # e) Retorne a soma dos quadrados dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma_dos_quadrados(self) -> int:
        sum: int = 0
        curr: Node | None = self.head
        while curr:
            sum += curr.key**2
            curr = curr.next
        return sum

    # (f) Elimine o k-esimo elemento da lista, se houver.
    # Considere que o primeiro elemento da lista esta na posicao 1
    def remove_k(self, k: int) -> None:
        if k < 1 or self.is_empty():
            return
        if k == 1:
            self.head = self.head.next
        else:
            pos: int = 1
            curr: Node = self.head
            while curr.next:
                pos += 1
                if pos == k:
                    curr.next = curr.next.next
                    break
                curr = curr.next

    # (g) Retire o elemento de maior valor da lista
    def remove_max(self) -> None:
        if self.is_empty():
            return
        curr = largest = self.head
        max: int = largest.key
        while curr.next:
            k: int = curr.next.key
            if k > max:
                max = k
                largest = curr.next
            curr = curr.next
        largest.key = self.head.key
        self.head = self.head.next

    # (h) Retire todos os elementos da lista com chave igual a um valor x, passado como parametro.
    # Para esta questao, considere que a lista pode conter mais de um elemento com mesmo valor de chave.
    def remove_todos_x(self, x: int) -> None:
        while self.head and self.head.key == x:
            self.head = self.head.next
        curr = self.head
        while curr and curr.next:
            if curr.next.key == x:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # (i) Reorganize a lista de forma que os elementos com chaves pares fiquem antes de elementos com chaves impares.
    def reorganiza_pares_antes(self) -> None:
        prev, curr = None, self.head
        while curr:
            if curr.key % 2 == 0:
                if not prev:
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr.next = self.head
                    self.head = curr
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next

    # (j) Modifique a lista de tal forma que todo elemento da lista com chave maior do que k venha antes
    # dos elementos na lista com chaves menores ou iguais a k.
    # O valor de k deve ser passado como parametro para a funcao.
    #
    # Em cada grupo de elementos - maiores do que k e menores ou iguais a k) -
    # a funcao deve manter a ordem original relativa dos elementos.
    def reorganiza_maiores_que_k_antes(self, k: int) -> None:
        maiores = ult = None
        prev, curr = None, self.head
        while curr:
            next = curr.next
            if curr.key > k:
                curr.next = None
                if prev:
                    prev.next = next
                else:
                    self.head = next

                if ult:
                    ult.next = curr
                    ult = curr
                else:
                    maiores = ult = curr
            else:
                prev = curr
            curr = next
        if maiores:
            ult.next = self.head
            self.head = maiores

    # (k) Inverta os elementos da lista
    def inverte_elementos(self) -> None:
        prev, curr = None, self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # (l) Reordene os elementos da lista, de forma que, se houver elementos na lista cujas chaves sejam
    # divisiveis por 10, estes devem vir antes dos outros elementos.
    def reordena_divisiveis_por_10_antes(self) -> None:
        prev, curr = None, self.head
        while curr:
            if curr.key % 10 == 0:
                if not prev:
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr.next = self.head
                    self.head = curr
                    curr = prev.next
            else:
                prev, curr = curr, curr.next

    # (m) Duplique elementos com chave igual a x na lista. Especificamente, para cada elemento 'e' da lista
    # com valor de chave igual a x, essa funcao cria um novo elemento com valor de chave igual a x e
    # o insere apos 'e' na lista. O valor de x deve ser passado como parametro da funcao.
    def duplica_todos_x(self, x: int) -> None:
        curr = self.head
        while curr:
            if curr.key == x:
                node = Node(x)
                node.next = curr.next
                curr.next = node
                curr = node.next
            else:
                curr = curr.next
