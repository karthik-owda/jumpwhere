# contains nearby duplicate
def contains_nearby_duplicate(nums, k):
    seen = set()

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i

    return False
