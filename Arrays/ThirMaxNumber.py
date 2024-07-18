# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned 



class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        
        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max and num != first_max:
                third_max = second_max
                second_max = num
            elif num > third_max and num != first_max and num != second_max:
                third_max = num
            
        return third_max if third_max != float('-inf') else first_max

  
                