# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       for i in range(len(flowerbed)):
            if n == 0:
                return True
            if ((i == 0 or flowerbed[i - 1] == 0)   # If at the first element or the previous element equals to 0
                and (flowerbed[i] == 0)             # If current element equals to 0
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)): # If at the last element or the next element equals to 0
                # Place flower at the current position
                flowerbed[i] = 1
                n -= 1

       return n == 0
            


            