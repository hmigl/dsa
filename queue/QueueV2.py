class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None


class QueueV2:
    def __init__(self) -> None:
        self.top: Node | None = None
        self.bottom: Node | None = None

    def is_empty(self) -> bool:
        return self.top is None

    def enqueue(self, x: int) -> bool:
        node: Node = Node(x)

        if self.is_empty():
            self.top = node
        else:
            self.bottom.next = node
        self.bottom = node
        return True

    def dequeue(self) -> tuple[bool, Node | None]:
        node: Node | None = self.top
        if node is None:
            return (False, None)

        self.top = self.top.next
        if self.is_empty():
            self.bottom = None
        return (True, node)

    def print(self) -> None:
        curr: Node | None = self.top
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.next
        print()
