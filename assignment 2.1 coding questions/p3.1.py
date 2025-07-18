import heapq

def find_kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]
arr = list(map(int, input("Enter the array elements: ").split()))
k = int(input("Enter the value of k: "))
print(f"The {k}th largest element is:", find_kth_largest(arr, k))
