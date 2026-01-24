# Ransom Note Problem in Python with Tests

def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    mag_count = Counter(magazine)
    for c in ransomNote:
        if mag_count[c] == 0:
            return False
        mag_count[c] -= 1
    return True

# Tests
def test_canConstruct():
    assert canConstruct("a", "b") == False
    assert canConstruct("aa", "ab") == False
    assert canConstruct("aa", "aab") == True
    assert canConstruct("", "anything") == True
    assert canConstruct("abc", "cba") == True
    assert canConstruct("aabbcc", "abcabc") == True
    assert canConstruct("aabbcc", "abccbaab") == True
    assert canConstruct("xyz", "xy") == False
    print("All tests passed!")

test_canConstruct()

