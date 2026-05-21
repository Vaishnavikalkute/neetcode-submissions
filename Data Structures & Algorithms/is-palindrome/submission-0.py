class Solution:
    def isPalindrome(self, s: str) -> bool:
        val="".join([char.lower() for char in s if char.isalnum()])

        if val==val[::-1]:
            return True
        return False