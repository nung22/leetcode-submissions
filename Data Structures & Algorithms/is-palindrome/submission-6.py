class Solution:
    def isPalindrome(self, s: str) -> bool:
        a_num_str = ""

        for char in s:
            if char.isalnum():
                a_num_str += char.lower()
        
        for i in range(len(a_num_str) // 2):
            if a_num_str[i] != a_num_str[-i - 1]:
                return False
        
        return True