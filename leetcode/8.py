# Medium

class Solution():
    def myAtoi(self, s: str) -> int:
        results = 0
        s = ''.join(s.split())
        print(s)
        if s[0].isalpha():
            return results
        for i in range(0,len(s)):
            


s = "      -2322 42asdasd    asdasda   -12312"
sol = Solution()
print(sol.myAtoi(s))
