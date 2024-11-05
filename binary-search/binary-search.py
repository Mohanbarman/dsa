def find_element(arr: list[int], target: int) -> int:
    lo = 0
    hi = len(arr) - 1

    while (lo <= hi):
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


input_arr = [2, 3, 4, 5, 5, 23, 23, 26, 45, 45, 345, 2345]
input_arr_1 = [2, 3, 4, 5]

print(find_element(input_arr, 2345))
