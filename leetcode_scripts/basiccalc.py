def calculate(s):
    """
    Basic calculator to evaluate a simple expression string containing non-negative integers,
    '+', '-', '(', ')', and spaces.
    """
    stack = []
    result = 0
    number = 0
    sign = 1  # 1 means positive, -1 means negative

    i = 0
    while i < len(s):
        char = s[i]
        if char.isdigit():
            number = 0
            while i < len(s) and s[i].isdigit():
                number = number * 10 + int(s[i])
                i += 1
            result += sign * number
            continue  # already incremented i
        elif char == '+':
            sign = 1
        elif char == '-':
            sign = -1
        elif char == '(':
            # Push the result and sign onto the stack, for later
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result
        # ignore spaces
        i += 1
    return result

# Tests
def test_calculate():
    assert calculate("1 + 1") == 2
    assert calculate(" 2-1 + 2 ") == 3
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert calculate("2-(5-6)") == 3
    assert calculate("  30") == 30
    assert calculate("-(2+3)") == -5
    assert calculate("1-(5)") == -4
    assert calculate("0") == 0
    assert calculate("2147483647") == 2147483647
    assert calculate("1-(     -2)") == 3
    print("All tests passed!")

test_calculate()
