"""
∀ k ∈  [1, i) A[k] ≠ ν
"""


def linear_search(A: list[int], v: int) -> int | None:
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None


A: list[int] = [int(n) for n in input().split()]
v: int = int(input())
print(linear_search(A, v))
