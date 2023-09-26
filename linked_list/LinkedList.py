class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None

    def get_key(self) -> int:
        return self.key


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def search(self, x: int) -> Node | None:
        curr: Node | None = self.head
        while (curr is not None) and (curr.get_key() != x):
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
        if self.head.get_key() == x:
            self.head = self.head.next
            return
        curr: Node = self.head
        while curr.next is not None:
            if curr.next.get_key() == x:
                curr.next = curr.next.next
                return
            curr = curr.next

    def rem(self, x: int) -> None:
        node: Node | None = self.search(x)
        if node:
            node.key = self.head.get_key()
            self.head = self.head.next

    def print(self) -> None:
        curr: Node | None = self.head
        while curr is not None:
            print(curr.get_key())
            curr = curr.next

    # a) Retorne o menor elemento da lista. Se a lista nao tiver elementos,
    # a funcao deve retornar uma indicacao de que a lista esta vazia
    def min(self) -> tuple[bool, int]:
        if self.is_empty():
            return (False, -1)
        curr, min = self.head, self.head.get_key()
        while curr:
            k: int = curr.get_key()
            if k < min:
                min = k
            curr = curr.next
        return (True, min)

    # b) Retorne o numero de elementos com chave ımpar na lista
    def chaves_impares(self) -> int:
        n: int = 0
        curr: Node | None = self.head
        while curr:
            if curr.get_key() % 2 != 0:
                n += 1
            curr = curr.next
        return n

    # c) Retorne a media dos valores na lista. Se a lista estiver vazia, o valor da media deve
    # ser considerado como sendo zero.
    def media(self) -> float:
        sum = i = 0
        curr: Node | None = self.head
        while curr:
            sum += curr.get_key()
            i += 1
            curr = curr.next
        return sum / i if i > 0 else 0

    # d) Retorna a soma dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma(self) -> int:
        sum: int = 0
        curr: Node | None = self.head
        while curr:
            sum += curr.get_key()
            curr = curr.next
        return sum

    # e) Retorne a soma dos quadrados dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma_dos_quadrados(self) -> int:
        sum: int = 0
        curr: Node | None = self.head
        while curr:
            sum += curr.get_key() ** 2
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
        max: int = largest.get_key()
        while curr.next:
            k: int = curr.next.get_key()
            if k > max:
                max = k
                largest = curr.next
            curr = curr.next
        largest.key = self.head.get_key()
        self.head = self.head.next

    # (h) Retire todos os elementos da lista com chave igual a um valor x, passado como parametro.
    # Para esta questao, considere que a lista pode conter mais de um elemento com mesmo valor de chave.
    def remove_todos_x(self, x: int) -> None:
        while self.head and self.head.get_key() == x:
            self.head = self.head.next
        curr = self.head
        while curr and curr.next:
            if curr.next.get_key() == x:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # (i) Reorganize a lista de forma que os elementos com chaves pares fiquem antes de elementos com chaves impares.
    def reorganiza_pares_antes(self) -> None:
        prev, curr = None, self.head
        while curr:
            if curr.get_key() % 2 == 0:
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


    # (k) Inverta os elementos da lista
    def inverte_elementos(self) -> None:
        prev, curr = None, self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
