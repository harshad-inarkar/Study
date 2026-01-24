def minMutation(startGene, endGene, bank):
    """
    Returns the minimum number of mutations needed to mutate from start to end.
    Each mutation changes a single character and must be in the bank.
    :type start: str
    :type end: str
    :type bank: List[str]
    :rtype: int
    """
    from collections import deque

    bank_set = set(bank)

    if endGene not in bank_set:
        return -1

    if startGene == endGene:
        return 0

    dq = deque()
    genes = ['A', 'C','G', 'T']
    dq.append((startGene,0)) # start and 0 muts


    while dq:
        gs , muts = dq.popleft()
        gs_list = list(gs)  # optimise mutation logic use mutable list
        
        i  = len(gs) -1
        while i != -1:
            orig_ch = gs_list[i]

            for g in genes:
                if g == orig_ch:
                    continue

                gs_list[i] = g
                ms = ''.join(gs_list)

                if ms == endGene:
                    return muts+1

                if ms in bank_set:
                    dq.append((ms,muts+1))
                    bank_set.remove(ms)

            gs_list[i] = orig_ch
            i-=1
    
    return -1


# Tests
def test_minMutation():
    # Test 1: Example from Leetcode
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    assert minMutation(start, end, bank) == 1, "Test 1 failed"

    # Test 2: Two-step mutation
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    assert minMutation(start, end, bank) == 2, "Test 2 failed"

    # Test 3: No possible mutation
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    assert minMutation(start, end, bank) == 3, "Test 3 failed"

    # Test 4: End not in bank
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC"]
    assert minMutation(start, end, bank) == -1, "Test 4 failed"

    # Test 5: Start equals end
    start = "AACCGGTT"
    end = "AACCGGTT"
    bank = ["AACCGGTT"]
    assert minMutation(start, end, bank) == 0, "Test 5 failed"

    # Test 6: No bank
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = []
    assert minMutation(start, end, bank) == -1, "Test 6 failed"

    print("All tests passed.")

if __name__ == "__main__":
    test_minMutation()
