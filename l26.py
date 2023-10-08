def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} found in position {result}.")
else:
    print(f"Element {target} not found.")


def fibonacci_search(arr, target):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_current = fib_m_minus_1 + fib_m_minus_2

    while fib_current < len(arr):
        fib_m_minus_2, fib_m_minus_1 = fib_m_minus_1, fib_current
        fib_current = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib_current > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < target:
            fib_current, fib_m_minus_1, fib_m_minus_2 = (
                fib_m_minus_1 - fib_m_minus_2,
                fib_m_minus_2,
                fib_m_minus_1 - fib_m_minus_2,
            )
            offset = i
        elif arr[i] > target:
            fib_current, fib_m_minus_1, fib_m_minus_2 = (
                fib_m_minus_2,
                fib_m_minus_1 - fib_m_minus_2,
                fib_m_minus_2 - (fib_m_minus_1 - fib_m_minus_2),
            )
        else:
            return i

    if (
        offset >= 0
        and arr[offset] == target
    ):
        return offset

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = fibonacci_search(arr, target)
if result != -1:
    print(f"Element {target} found in position {result}.")
else:
    print(f"Element {target} not found.")

