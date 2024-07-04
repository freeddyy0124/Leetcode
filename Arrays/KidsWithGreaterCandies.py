# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

 

# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        # use method below if I am able to use this built in method
        # max_candies = max(candies)
        for n in candies:
            maxCandy = max(maxCandy, n)
        res = []
        for n in candies:
            currTotal = n + extraCandies
            if currTotal >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res

        