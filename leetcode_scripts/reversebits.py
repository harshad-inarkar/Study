def reverse_bits(n, num_bits=32):
    result = 0
    for i in range(num_bits):
        result = (result << 1) | (n &1)
        n = n >> 1

    return result

# Tests
def test_reverse_bits():
    # 43261596 (0b00000010100101000001111010011100) reversed is 964176192 (0b00111001011110000010100101000000)
    assert reverse_bits(43261596) == 964176192
    # 0 reversed is 0
    assert reverse_bits(0) == 0
    # 1 reversed in 32 bits is 2147483648
    assert reverse_bits(1) == 2147483648
    # All bits set
    assert reverse_bits(0xFFFFFFFF) == 0xFFFFFFFF
    # 0b101 (5) reversed in 8 bits is 0b10100000 (160)
    assert reverse_bits(0b101, 8) == 160
    print("All tests passed.")

if __name__ == "__main__":
    test_reverse_bits()
