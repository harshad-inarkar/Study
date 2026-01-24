def fullJustify(words: list[str], maxWidth: int) -> list[str]:
    result = []
    current_line = []
    current_length = 0
    
    for word in words:
        # Check if adding this word would exceed maxWidth
        if current_length + len(word) + len(current_line) > maxWidth:
            # Process current line
            if len(current_line) == 1:
                # Single word case - left justify
                result.append(current_line[0] + ' ' * (maxWidth - current_length))
            else:
                # Multiple words - distribute spaces evenly
                spaces_needed = maxWidth - current_length
                spaces_per_gap = spaces_needed // (len(current_line) - 1)
                extra_spaces = spaces_needed % (len(current_line) - 1)
                
                line = current_line[0]
                for i in range(1, len(current_line)):
                    spaces = spaces_per_gap + (1 if i <= extra_spaces else 0)
                    line += ' ' * spaces + current_line[i]
                result.append(line)
            
            # Reset for next line
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)
    
    # Handle last line (left justified)
    if current_line:
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
    
    return result

# Test cases
def test_fullJustify():
    # Test case 1: Basic case
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    expected = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]
    assert fullJustify(words, maxWidth) == expected
    
    # Test case 2: Single word per line
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    expected = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]
    assert fullJustify(words, maxWidth) == expected
    
    # Test case 3: Empty input
    assert fullJustify([], 16) == []
    
    print("All test cases passed!")

# Run the tests
test_fullJustify()
