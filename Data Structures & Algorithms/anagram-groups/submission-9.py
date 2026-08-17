class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_str = "".join(sorted(word))
            anagrams[sorted_str] = anagrams.get(sorted_str, []) + [word]
        
        return list(anagrams.values())