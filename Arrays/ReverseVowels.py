# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowel = 'aeiouAEIOU'
        list_s = list(s)

        while l < r:
            while l < r and list_s[l] not in vowel:
                l += 1
            while l < r and list_s[r] not in vowel:
                r -= 1
            list_s[l], list_s[r] = list_s[r], list_s[l]
            l += 1
            r -= 1
        return ''.join(list_s)