class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None


class QueueV2:
    def __init__(self) -> None:
        self.front: Node | None = None
        self.back: Node | None = None

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, x: int) -> bool:
        node: Node = Node(x)

        if self.is_empty():
            self.front = node
        else:
            self.back.next = node
        self.back = node
        return True

    def dequeue(self) -> tuple[bool, Node | None]:
        node: Node | None = self.front
        if node is None:
            return (False, None)

        self.front = self.front.next
        if self.is_empty():
            self.back = None
        return (True, node)

    def print(self) -> None:
        curr: Node | None = self.front
        while curr is not None:
            print(curr.key, end=" ")
            curr = curr.next
        print()
