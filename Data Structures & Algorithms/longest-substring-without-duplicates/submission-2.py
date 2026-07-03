class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        l = 0
        for index, char in enumerate(s):
            while char in s[l:index]:
                l += 1
            longest_substring = max(longest_substring, len(s[l:index]) + 1)
        return longest_substring
