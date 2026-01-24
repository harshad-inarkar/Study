def isValid(s):
    """
    Determines if the input string s containing just the characters '(', ')', '{', '}', '[' and ']'
    is valid. An input string is valid if:
      1. Open brackets are closed by the same type of brackets.
      2. Open brackets are closed in the correct order.
    """
    stack = []
    par_map = {')':'(', '}': '{', ']':'[' }

    for c in s:
        if c in par_map.values():
            stack.append(c)
        elif c in par_map:
            if stack and par_map[c] == stack[-1]:
                stack.pop()
            else:
                return False
    
    return not stack

# Tests
def test_isValid():
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([)]") == False
    assert isValid("{[]}") == True
    assert isValid("") == True
    assert isValid("(((((())))))") == True
    assert isValid("(((()") == False
    assert isValid("]") == False
    assert isValid("[") == False
    print("All tests passed!")

test_isValid()
