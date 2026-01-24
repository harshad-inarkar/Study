def evalRPN(tokens):
    """
    Evaluates the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
    Division between two integers should truncate toward zero.
    Args:
        tokens (List[str]): The list of tokens in RPN order.
    Returns:
        int: The result of the expression.
    """
    stack = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Truncate towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

# Tests
def test_evalRPN():
    assert evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert evalRPN(["3", "-4", "+"]) == -1
    assert evalRPN(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14
    assert evalRPN(["4", "2", "/"]) == 2
    assert evalRPN(["4", "-2", "/"]) == -2
    assert evalRPN(["-4", "2", "/"]) == -2
    assert evalRPN(["-4", "-2", "/"]) == 2
    print("All tests passed!")

test_evalRPN()
