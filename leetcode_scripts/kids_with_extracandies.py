def kids_with_candies(candies, extra_candies):
    """
    Given the array candies and the integer extra_candies, where candies[i] represents the number of candies that the i-th kid has.
    Return a boolean list indicating whether each child could have the greatest number of candies among all the kids
    if they were given all extra_candies.
    """
    max_candies = max(candies)
    return [c + extra_candies >= max_candies for c in candies]

def test_kids_with_candies():
    assert kids_with_candies([2,3,5,1,3], 3) == [True, True, True, False, True]
    assert kids_with_candies([4,2,1,1,2], 1) == [True, False, False, False, False]
    assert kids_with_candies([12,1,12], 10) == [True, False, True]
    assert kids_with_candies([], 3) == []
    assert kids_with_candies([1], 0) == [True]
    print("All tests passed for kids_with_candies.")

if __name__ == "__main__":
    test_kids_with_candies()
