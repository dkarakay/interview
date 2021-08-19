# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)

        while left < n and right < n:
            char = s[right]
            if char in m:
                left = max(left, m[char] + 1)
            m[char] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
