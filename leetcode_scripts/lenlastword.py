def lengthOfLastWord(s: str) -> int:
    # Split the string into words and filter out empty strings
    words = [word for word in s.split() if word]
    
    # If there are no words, return 0
    if not words:
        return 0
    
    # Return the length of the last word
    return len(words[-1])
