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
        if self.search(x):
            return False
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
        if self.search(x):
            return False
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

