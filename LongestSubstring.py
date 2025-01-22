left = max_length = 0
char_set = set()
s = "abcabcbb"

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)