def move_zeroes(nums):
    """
    Moves all zeroes in the list nums to the end while maintaining the relative 
    order of the non-zero elements. Modifies nums in-place.
    """
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0

def test_move_zeroes():
    arr1 = [0,1,0,3,12]
    move_zeroes(arr1)
    assert arr1 == [1,3,12,0,0]

    arr2 = [0,0,1]
    move_zeroes(arr2)
    assert arr2 == [1,0,0]

    arr3 = [1,2,3]
    move_zeroes(arr3)
    assert arr3 == [1,2,3]

    arr4 = [0,0,0]
    move_zeroes(arr4)
    assert arr4 == [0,0,0]

    arr5 = []
    move_zeroes(arr5)
    assert arr5 == []

    arr6 = [1,0,0,0,5]
    move_zeroes(arr6)
    assert arr6 == [1,5,0,0,0]

    arr7 = [0,0,0,1]
    move_zeroes(arr7)
    assert arr7 == [1,0,0,0]

    arr8 = [4,2,4,0,0,3,0,5,1,0]
    move_zeroes(arr8)
    assert arr8 == [4,2,4,3,5,1,0,0,0,0]

    print("All tests passed for move_zeroes.")

if __name__ == "__main__":
    test_move_zeroes()
