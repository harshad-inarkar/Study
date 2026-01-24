def convert(s: str, numRows: int) -> str:
    if numRows <= 1 or numRows >= len(s):
        return s
    
    rows = [''] * numRows
    cur, step = 0,1
    

    for c in s:
        rows[cur] += c

        if cur == 0:
            step =1 
        elif cur == numRows -1:
            step =-1
        
        cur+=step

    return ''.join(rows)



# Test cases
def test_convert():
    # Test case 1: Basic zigzag
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    
    # Test case 2: Single row
    assert convert("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    
    # Test case 3: Two rows
    assert convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    
    # Test case 4: Empty string
    assert convert("", 3) == ""
    
    # Test case 5: String shorter than numRows
    assert convert("ABC", 4) == "ABC"
    
    print("All test cases passed!")

# Run the tests
test_convert()
