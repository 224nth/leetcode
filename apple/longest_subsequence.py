

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        map = {}
        start = 0

        for i in range(len(s)):
            if s[i] in map.keys():
                start = max(start, map[s[i]] +1)

            map[s[i]] = i
            longest = max(longest, i-start+1)

        return longest

assert Solution().lengthOfLongestSubstring("pwwkew") ==3
assert Solution().lengthOfLongestSubstring("abcabcbb") ==3
assert Solution().lengthOfLongestSubstring("bbbbb") ==1
