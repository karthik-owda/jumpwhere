import math

def getPermutation(n, k):
    numbers = list(range(1, n + 1))
    k -= 1
    result = ""
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        result += str(numbers[index])
        numbers.pop(index)
        k %= fact
    return result
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))
print("The", k, "th permutation is:", getPermutation(n, k))
