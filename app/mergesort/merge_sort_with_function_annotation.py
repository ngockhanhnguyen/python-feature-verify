

def merge_sort(arr: list, l: int, r: int):
    if l < r:
        m = int((l + r) / 2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr: list, l: int, m: int, r: int):
    temp_arr = list()
    i = l
    j = m + 1
    while i <= m or j <= r:
        if i > m:
            temp_arr.extend(arr[j:r + 1])
            break
        if j > r:
            temp_arr.extend(arr[i:m + 1])
            break
        if arr[i] < arr[j]:
            temp_arr.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            temp_arr.append(arr[j])
            j += 1

    print(temp_arr)
    for i in range(0, len(temp_arr)):
        arr[i + l] = temp_arr[i]
    print(arr)
    print()


if __name__ == "__main__.py":
    arr_test = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr_test, 0, len(arr_test) - 1)
    print(arr_test)
