# 이진 탐색 binary search
# try to find 'target' in 'arr'

def binary_search(arr, target):
    # set search range
    start = 0
    end = len(arr) - 1

    # keep searching until
    # there is no more indices left to search
    # which means 'start' becomes bigger than 'end'
    while start <= end:
        # find the middle index
        mid = (start + end) // 2

        # if data at the 'mid' is 'target
        if arr[mid] == target:
            return mid

        # else adjust indices
        # if data at 'mid' is bigger than 'target'
        if arr[mid] > target:

        # set 'end' = 'mid - 1'
            end = mid - 1
        # else if data at 'mid' is smaller than 'target'
        elif arr[mid] < target:
        # set 'start' to 'mid + 1'
            start = mid + 1


