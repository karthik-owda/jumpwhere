def find_start(arr, target):
    left, right = 0, len(arr) - 1
    start = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            start = mid
            right = mid - 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return start

def find_end(arr, target):
    left, right = 0, len(arr) - 1
    end = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            end = mid
            left = mid + 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return end

def first_and_last(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr, target)
    end = find_end(arr, target)
    return [start, end]
