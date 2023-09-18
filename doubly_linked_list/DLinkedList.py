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

    def print(self) -> None:
        curr: Node | None = self.head
        while curr is not None:
            print(curr.key)
            curr = curr.next
