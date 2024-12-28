class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if int(x) < 0:
            return False
        for i in range(len(x) // 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True


objet = Solution()
print(objet.isPalindrome(x=121))
