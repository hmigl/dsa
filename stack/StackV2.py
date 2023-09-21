class Node:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.next: Node | None = None


class StackV2:
    def __init__(self) -> None:
        self.top: Node | None = None
        self.bottom: Node | None = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, x: int) -> bool:
        node: Node = Node(x)

        if self.is_empty():
            self.bottom = node
        node.next = self.top
        self.top = node

        return True

    def pop(self) -> Node | None:
        if self.is_empty():
            return None

        removed: Node = self.top
        self.top = self.top.next
        if self.top is None:
            self.bottom = None

        return removed

    def print(self) -> None:
        curr: Node | None = self.top
        while curr is not None:
            print(curr.key)
            curr = curr.next
