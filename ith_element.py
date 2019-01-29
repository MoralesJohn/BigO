# arr = [-1, 0, 1, 3, 5, 7, 8, 9, 99, 999]
# arr = [0, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 9]
arr = [-1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_ith_match(a):
    if a[0] > 0:
        return False
    start_ndx = 0
    end_ndx = len(a) - 1
    if a[end_ndx] < end_ndx:
        return False
    while start_ndx <= end_ndx:
        split_ndx = start_ndx + ((end_ndx - start_ndx) // 2)
        val = a[split_ndx]
        if split_ndx == val:
            return True
        if split_ndx < val:
            end_ndx = min(split_ndx, end_ndx - 1)
            continue
        start_ndx = max(split_ndx, start_ndx + 1)
    return False

print(arr, find_ith_match(arr))


