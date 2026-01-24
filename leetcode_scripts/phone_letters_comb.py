def letterCombinations(digits):
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return []
 
    def get_letters(d):
        d = int(d) #ord(d) - ord('0')
        offset =  3 * (d-2)
        
        if d in (8,9) : offset+=1
        count = 4 if d in (7,9) else 3

        for i in range(count):
            yield chr(ord('a')+offset+i)

    res = []
    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return
        for ch in get_letters(digits[index]):
            backtrack(index+1, path+ch)
            
    backtrack(0, "")
    return res

# Tests
def test_letterCombinations():
    assert sorted(letterCombinations("23")) == sorted([
        "ad","ae","af","bd","be","bf","cd","ce","cf"
    ]), "Test 1 failed"
    assert letterCombinations("") == [], "Test 2 failed"
    assert sorted(letterCombinations("2")) == sorted(["a","b","c"]), "Test 3 failed"
    assert sorted(letterCombinations("7")) == sorted(["p","q","r","s"]), "Test 4 failed"
    assert sorted(letterCombinations("79")) == sorted([
        "pw","px","py","pz",
        "qw","qx","qy","qz",
        "rw","rx","ry","rz",
        "sw","sx","sy","sz"
    ]), "Test 5 failed"
    print("All tests passed.")

if __name__ == "__main__":
    test_letterCombinations()
