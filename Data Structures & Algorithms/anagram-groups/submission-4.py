class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams.keys():
                anagrams[sorted_s] = [s]
            else:
                anagrams[sorted_s] = anagrams.get(sorted_s) + [s]

        return list(anagrams.values())