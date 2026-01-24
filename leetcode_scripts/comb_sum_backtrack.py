def combination_sum(candidates, target):
    if not candidates or target <= 0:
        return []


    result = []
    candidates.sort()
    n = len(candidates)
    
    # max len = targt/min +1
    path = [0]* (target//candidates[0] +1)


    def backtrack(start, remaining, pathlen):
        if remaining == 0:
            result.append(path[:pathlen])
            return


        for i in range(start, n):
            if candidates[i] > remaining:
                break
            path[pathlen] = candidates[i]

            backtrack(i, remaining - candidates[i], pathlen+1)
    
    backtrack(0,target, 0)
    return result

# Tests
def test_combination_sum():
    assert sorted(combination_sum([2,3,6,7], 7)) == sorted([[2,2,3],[7]])
    assert sorted(combination_sum([2,3,5], 8)) == sorted([[2,2,2,2],[2,3,3],[3,5],[2,2,3,1]]) or sorted(combination_sum([2,3,5], 8)) == sorted([[2,2,2,2],[2,3,3],[3,5]])
    assert combination_sum([2], 1) == []
    assert combination_sum([1], 1) == [[1]]
    assert sorted(combination_sum([2,3], 6)) == sorted([[2,2,2],[3,3]])

test_combination_sum()
print("All tests passed.")
