from collections import Counter
def minWindow(s, t):
    if not s or not t:
        return ""
    t_count = Counter(t)
    required = len(t_count)
    left = 0
    formed = 0
    window_counts = {}
    min_len = float("inf")
    min_window = (0, 0)

    right = 0
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                formed -= 1
            left += 1
        right += 1
    l, r = min_window
    return s[l:r+1] if min_len != float("inf") else ""

s = input("Enter string s: ")
t = input("Enter string t: ")
print("Minimum window substring:", minWindow(s, t))
