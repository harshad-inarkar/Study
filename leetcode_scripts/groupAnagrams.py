def groupAnagrams(strs):
    """
    Groups anagrams together from the input list of strings.
    Returns a list of lists of anagrams.
    """
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        # Use tuple of sorted characters as the key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

# Tests
def test_groupAnagrams():
    result1 = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    expected1 = [["eat","tea","ate"],["tan","nat"],["bat"]]
    # Convert inner lists to sets for comparison
    assert sorted([set(g) for g in result1]) == sorted([set(g) for g in expected1])

    result2 = groupAnagrams([""])
    expected2 = [[""]]
    assert sorted([set(g) for g in result2]) == sorted([set(g) for g in expected2])

    result3 = groupAnagrams(["a"])
    expected3 = [["a"]]
    assert sorted([set(g) for g in result3]) == sorted([set(g) for g in expected3])

    result4 = groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz", "foo", "ofo"])
    expected4 = [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"], ["foo", "ofo"]]
    assert sorted([set(g) for g in result4]) == sorted([set(g) for g in expected4])

    print("All tests passed!")

test_groupAnagrams()
