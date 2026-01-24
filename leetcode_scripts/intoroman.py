def intToRoman(num: int) -> str:
    """
    Convert an integer to a Roman numeral.
    
    Parameters:
        num: int - Integer to be converted (1 <= num <= 3999)
    Returns:
        str - The Roman numeral representation of the integer
    """
    # Define the mapping of values to Roman numerals
    # Using tuples to maintain order
    val_map = (
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'),  (90, 'XC'), (50, 'L'),  (40, 'XL'),
            (10, 'X'),   (9, 'IX'),  (5, 'V'),   (4, 'IV'),
            (1, 'I')
        )

    result = []
    for value, symbol in val_map:
        while num >= value:
            result.append(symbol)
            num -= value 

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    number = 1994
    result = intToRoman(number)
    print(f"The Roman numeral representation of {number} is: {result}")  # Output: MCMXCIV
