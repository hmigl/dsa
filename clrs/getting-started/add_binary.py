def add_binary(A: list[int], B: list[int]) -> list[int]:
    n: int = len(A)
    C: list[int] = [0] * (n + 1)
    carry: int = 0

    i: int = n - 1
    while i >= 0:
        sum: int = A[i] + B[i] + carry
        C[i + 1] = sum % 2
        carry = sum // 2
        i -= 1

    C[0] = carry
    return C


A: list[int] = [1, 0, 1]
B: list[int] = [1, 0, 1]
C: list[int] = add_binary(A, B)

print(C)
