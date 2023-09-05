class Stack:
    def __init__(self, maxnelems: int) -> None:
        self.nelemns: int = 0
        self.data: list[int] = [0] * maxnelems

    def push(self, x: int) -> bool:
        if self.nelemns == len(self.data):
            return False
        self.data[self.nelemns] = x
        self.nelemns += 1
        return True

    def pop(self) -> bool | tuple[bool, int]:
        if self.nelemns == 0:
            return False
        self.nelemns -= 1
        return (True, self.data[self.nelemns])
