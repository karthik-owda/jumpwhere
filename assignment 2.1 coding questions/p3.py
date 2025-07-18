def find_kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
arr = list(map(int, input("Enter the array elements: ").split()))
k = int(input("Enter the value of k: "))
print(f"The {k}th largest element is:", find_kth_largest(arr, k))
