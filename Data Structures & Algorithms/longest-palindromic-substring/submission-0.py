class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        middle = n // 2  # 3 => 1; 4 => 2
        if n % 2 == 1: 
            res = s[middle]
            l, r = middle-1, middle+1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                res = s[l] + res + s[r]
                l -= 1
                r += 1
        else:
            res = ""
            l, r = middle, middle
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                res = s[l] + res + s[r]
                l -= 1
                r += 1
        
        return res