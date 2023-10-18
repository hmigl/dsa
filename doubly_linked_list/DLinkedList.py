class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None
        self.prev: Node | None = None


class DLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        # self.tail: Node | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def search(self, x: int) -> bool:
        curr: Node | None = self.head
        while curr and curr.key != x:
            curr = curr.next
        return curr is not None

    def find(self, x: int) -> Node | None:
        curr: Node | None = self.head
        while curr and curr.key != x:
            curr = curr.next
        return curr

    def insert_front(self, x: int) -> bool:
        if self.search(x):
            return False
        node: Node = Node(x)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        return True

    def insert_back(self, x: int) -> bool:
        if self.search(x):
            return False
        node: Node = Node(x)
        if self.is_empty():
            self.head = node
        else:
            curr: Node = self.head
            while curr.next is not None:
                curr = curr.next
            node.prev = curr
            curr.next = node
        return True

    def remove(self, x: int) -> bool:
        if self.is_empty():
            return False

        if self.head.key == x:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return True

        curr = self.head
        while curr is not None:
            if curr.key == x:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return True
            curr = curr.next

        return False

    def remove_v2(self, x: int) -> bool:
        node: Node | None = self.find(x)

        if node is None:
            return False

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = self.head.next
        if node.next is not None:
            node.next.prev = node.prev
        return True

    def print(self) -> None:
        curr: Node | None = self.head
        while curr is not None:
            print(curr.key)
            curr = curr.next

    # a) Retorne o menor elemento da lista. Se a lista nao tiver elementos,
    # a funcao deve retornar uma indicacao de que a lista esta vazia
    def min(self) -> tuple[bool, int]:
        if not self.head:
            return (False, -1)
        curr = self.head
        min = curr.key
        while curr.next:
            if curr.next.key < min:
                min = curr.next.key
            curr = curr.next
        return (True, min)

    # b) Retorne o numero de elementos com chave ımpar na lista
    def chaves_impares(self) -> int:
        n = 0
        curr = self.head
        while curr:
            if curr.key % 2 != 0:
                n += 1
            curr = curr.next
        return n

    # c) Retorne a media dos valores na lista. Se a lista estiver vazia, o valor da media deve
    # ser considerado como sendo zero.
    def media(self) -> float:
        sum = i = 0
        curr = self.head
        while curr:
            sum += curr.key
            i += 1
            curr = curr.next
        return sum / i if i > 0 else 0

    # d) Retorna a soma dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma(self) -> int:
        sum = 0
        curr = self.head
        while curr:
            sum += curr.key
            curr = curr.next
        return sum

    # e) Retorne a soma dos quadrados dos valores armazenados na lista.
    # Se a lista estiver vazia, retorna o valor zero
    def soma_dos_quadrados(self) -> int:
        sum = 0
        curr = self.head
        while curr:
            sum += curr.key**2
            curr = curr.next
        return sum

    # (f) Elimine o k-esimo elemento da lista, se houver.
    # Considere que o primeiro elemento da lista esta na posicao 1
    def remove_k(self, k: int) -> None:
        curr, pos = self.head, 1
        while curr and k != pos:
            pos += 1
            curr = curr.next
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                self.head = self.head.next
            if curr.next:
                curr.next.prev = curr.prev

    # (g) Retire o elemento de maior valor da lista
    def remove_max(self) -> None:
        if not self.head:
            return

        curr = largest = self.head
        max = curr.key
        while curr.next:
            if curr.next.key > max:
                largest, max = curr.next, curr.next.key
            curr = curr.next

        if not largest.prev:
            self.head = self.head.next
        else:
            largest.prev.next = largest.next
            if largest.next:
                largest.next.prev = largest.prev

    # (h) Retire todos os elementos da lista com chave igual a um valor x, passado como parametro.
    # Para esta questao, considere que a lista pode conter mais de um elemento com mesmo valor de chave.
    def remove_todos_x(self, x: int) -> None:
        while self.head and self.head.key == x:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        curr = self.head
        while curr and curr.next:
            if curr.next.key == x:
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = curr
            else:
                curr = curr.next

