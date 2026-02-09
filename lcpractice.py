def two_sum(nums, target):
    # Dictionary to store number and its index
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Found the pair
        seen[num] = i
    
    return []  # No solution found