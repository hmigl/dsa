class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None

    def get_key(self) -> int:
        return self.key


class List:
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

    def print(self) -> None:
        curr: Node | None = self.head
        while curr is not None:
            print(curr.get_key())
            curr = curr.next
