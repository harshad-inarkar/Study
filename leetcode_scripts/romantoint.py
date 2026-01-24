def romanToInt(s: str) -> int:
    """
    Convert a Roman numeral to an integer.
    
    Parameters:
        s: str - Roman numeral as a string
    Returns:
        int - The integer representation of the Roman numeral
    """
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s:
        value = roman_to_int[char]
        total += value
        if value > prev_value:
            total -= 2 * prev_value

        prev_value = value
    
    return total

# Example usage
if __name__ == "__main__":
    roman_numeral = "MCMXCIV"
    result = romanToInt(roman_numeral)
    print(f"The integer value of the Roman numeral {roman_numeral} is: {result}")  # Output: 1994
