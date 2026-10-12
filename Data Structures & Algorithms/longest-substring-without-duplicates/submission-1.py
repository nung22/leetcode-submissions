class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        slow, fast = 0, 0
        longest = 0
        substr = set()

        while fast < len(s):
            if s[fast] not in substr:
                substr.add(s[fast])
                fast += 1
                longest = max(len(substr), longest)
            else:
                substr.remove(s[slow])
                slow += 1

        return longest