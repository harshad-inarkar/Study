def can_place_flowers(flowerbed, n):
    """
    Given a flowerbed (list of integers 0 and 1), and an integer n, 
    returns True if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
    """
    count = 0
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            prev = flowerbed[i-1] if i > 0 else 0
            nex = flowerbed[i+1] if i < length - 1 else 0
            if prev == 0 and nex == 0:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    return count >= n

def test_can_place_flowers():
    assert can_place_flowers([1,0,0,0,1], 1) == True
    assert can_place_flowers([1,0,0,0,1], 2) == False
    assert can_place_flowers([0,0,1,0,0], 2) == True
    assert can_place_flowers([0,0,0,0,0], 3) == True
    assert can_place_flowers([1,0,0,0,0,1], 2) == False
    assert can_place_flowers([1,0,1,0,1,0,1], 1) == False
    assert can_place_flowers([], 0) == True
    assert can_place_flowers([0], 1) == True
    assert can_place_flowers([1], 0) == True
    assert can_place_flowers([1], 1) == False
    print("All tests passed for can_place_flowers.")

if __name__ == "__main__":
    test_can_place_flowers()
