def reverse_vowels(s):
    """
    Reverses only the vowels in a given string s.
    """
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return "".join(s_list)

def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("leetcode") == "leotcede"
    assert reverse_vowels("aA") == "Aa"
    assert reverse_vowels("bcdfg") == "bcdfg"
    assert reverse_vowels("") == ""
    assert reverse_vowels("Eunoia") == "aiuonE"
    print("All tests passed for reverse_vowels.")

if __name__ == "__main__":
    test_reverse_vowels()
