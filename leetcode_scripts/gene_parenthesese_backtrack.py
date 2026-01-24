def generate_parentheses(n):
    """
    Generate all combinations of n pairs of well-formed parentheses.

    :param n: int
    :return: List[str]
    """
    result = []
    path = ['']* (2*n)

    def backtrack(pathlen,left, right):
        if pathlen == 2 * n:
            result.append(''.join(path))
            return
            
        if left < n: # add left
            path[pathlen] = '('
            backtrack(pathlen+1, left+1, right)
        if right < left: # add right
            path[pathlen] = ')'
            backtrack(pathlen+1, left, right+1)
    backtrack(0, 0, 0)
    return result

# Tests
def test_generate_parentheses():
    assert set(generate_parentheses(1)) == {"()"}
    assert set(generate_parentheses(2)) == {"(())", "()()"}
    assert set(generate_parentheses(3)) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert generate_parentheses(0) == [""]
    print("All tests passed.")

if __name__ == "__main__":
    test_generate_parentheses()
