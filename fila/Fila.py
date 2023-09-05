class Queue:
    def __init__(self, maxnelems: int) -> None:
        self.data: list[int] = [0] * maxnelems
        self.head: int = 0
        self.nelems: int = 0

    def enqueue(self, x: int) -> bool:
        if self.nelems == len(self.data):
            return False
        i: int = (self.head + self.nelems) % len(self.data)
        self.data[i] = x
        self.nelems += 1
        return True

    def dequeue(self) -> bool | tuple[bool, int]:
        if self.nelems == 0:
            return False
        x: int = self.data[self.head]
        self.head = (self.head + 1) % len(self.data)
        self.nelems -= 1
        return (True, x)

    def print(self) -> None:
        for i in range(self.nelems):
            print(self.data[(self.head + i) % len(self.data)])
