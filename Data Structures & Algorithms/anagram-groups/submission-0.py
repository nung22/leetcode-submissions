class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)  # key: sorted tuple of chars, value: list of anagrams
        for word in strs:
            key = tuple(sorted(word))  # sort chars to form key
            anagrams[key].append(word)
        return list(anagrams.values())  # return grouped anagrams
