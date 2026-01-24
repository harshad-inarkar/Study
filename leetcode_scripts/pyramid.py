def pyramid(n):
    """
    Prints a pyramid of height n using '*' characters.
    Each row is centered.
    """
    for i in range(1, n+1):
        stars = '*' * (2*i - 1)
        spaces = ' ' * (n - i)
        print(spaces + stars + spaces)

# Tests
def test_pyramid():
    print("Test 1: n = 1")
    pyramid(1)
    print("---")

    print("Test 2: n = 2")
    pyramid(2)
    print("---")

    print("Test 3: n = 3")
    pyramid(3)
    print("---")

    print("Test 4: n = 5")
    pyramid(5)
    print("---")

    print("Test 5: n = 0 (should print nothing)")
    pyramid(0)
    print("---")

test_pyramid()


