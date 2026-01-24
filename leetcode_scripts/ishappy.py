def isHappy(n: int) -> bool:
    """
    Determines if a number is a happy number.
    A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits,
    and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    """
    def get_sq_sum(n):
        sqsum = 0
        while n!=0:
            sqsum+=(n%10)**2
            n= n//10

        return sqsum
    
    slow = n
    fast =get_sq_sum(n)

    while fast != 1 and slow != fast:
        slow = get_sq_sum(slow)
        fast = get_sq_sum(get_sq_sum(fast))

    return fast == 1        

# Tests
def test_isHappy():
    assert isHappy(19) == True  # 19 is a happy number
    assert isHappy(2) == False  # 2 is not a happy number
    assert isHappy(1) == True   # 1 is a happy number
    assert isHappy(7) == True   # 7 is a happy number
    assert isHappy(4) == False  # 4 is not a happy number
    assert isHappy(100) == True # 100 is a happy number
    assert isHappy(1111111) == True # 1111111 is a happy number
    print("All tests passed!")

test_isHappy()
