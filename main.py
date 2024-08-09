# O(1) - константная сложность

def get_element(arr, index):
    return arr[index]


arrout = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("O(1) - константная сложность")
print(get_element(arrout, 4))


# O(n) - линейная сложность алгоритма
print("O(n) - линейная сложность алгоритма")


def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arrls = [10, 20, 30, 40, 50]
print(line_search(arrls, 30))
print(line_search(arrls, 60))

# O(log n) = логарифмическая сложность алгоритма
print("O(log n) = логарифмическая сложность алгоритма")


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arrbs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(arrbs, 70))  # выведет 6
print(binary_search(arrbs, 25))  # выведет -1
