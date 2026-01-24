def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_length = 0
    start = 0

    for i, c in enumerate(s):
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1
        char_index[c] = i
        max_length = max(max_length, i - start + 1)
    return max_length

# Example usage:
# print(length_of_longest_substring("abcabcbb"))  # Output: 3
