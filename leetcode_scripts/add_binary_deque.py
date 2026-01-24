from collections import deque

def add_binary_strings(a, b):
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = deque()

    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0

        total = bit_a ^ bit_b ^ carry
        carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)
        result.appendleft(str(total))
        i -= 1
        j -= 1

    return ''.join(result)

# Example usage:
# print(add_binary_strings("1011", "1101"))  # Output: "11000"

