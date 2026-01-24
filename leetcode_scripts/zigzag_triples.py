def zigzag_triples(numbers):
 
    """
    Given an array of integers numbers, returns an array of length len(numbers) - 2,
    where the ith element is 1 if (numbers[i], numbers[i+1], numbers[i+2]) is a zigzag triple,
    and 0 otherwise.
    """
    n = len(numbers)
    if n < 3:
        return []

    return [
        1 if (numbers[i] < numbers[i+1] > numbers[i+2]) or (numbers[i] > numbers[i+1] < numbers[i+2]) else 0
        for i in range(n - 2)
    ]


if __name__ == "__main__":
    def test_zigzag_triples():
        assert zigzag_triples([1, 3, 2, 4, 3]) == [1, 1, 1]
        assert zigzag_triples([1, 2, 3, 4, 5]) == [0, 0, 0]
        assert zigzag_triples([5, 1, 5, 1, 5]) == [1, 1, 1]
        assert zigzag_triples([1, 2, 1]) == [1]
        assert zigzag_triples([2, 2, 2]) == [0]
        assert zigzag_triples([1, 2]) == []
        assert zigzag_triples([]) == []
        assert zigzag_triples([1, 3, 2, 1, 2, 3, 2]) == [1, 0, 1, 0, 1]
        print("All zigzag_triples tests passed!")

    test_zigzag_triples()

 