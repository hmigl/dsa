def insertion_sort(arr: list[int]) -> None:
    for i in range(1, len(arr)):
        key: int = arr[i]
        j: int = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr: list[int] = [int(n) for n in input().split()]
insertion_sort(arr)
print(arr)
