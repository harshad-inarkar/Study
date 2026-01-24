def two_sum_sorted(numbers, target):
    l, r = 0, len(numbers)-1

    while l < r:
        tot = numbers[l] + numbers[r]
        if tot < target:
            l+=1
        elif tot > target:
            r-=1
        else:
            break
        
    return [l+1,r+1]
        

# Example usage:
print(two_sum_sorted([2, 7, 11, 15], 9))  # Output: [0, 1]
