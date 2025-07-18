def are_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1  # Corrected line
        else:
            freq2[ch] = 1
    
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True
s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")
if are_anagram(s1, s2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
