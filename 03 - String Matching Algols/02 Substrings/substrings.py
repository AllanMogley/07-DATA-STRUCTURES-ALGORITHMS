class Solution(s):
    def l_Subs(self, s):

        n = len(s)
        maxLength = 0
        left = 0
        charset = set()

        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                maxLength = max(maxLength, right - left + 1)

            else:
                while s[right] in charset:
                    charset.remove(s[right])
                    left += 1
                    charset.add(s[right])

        return(maxLength)

word = Solution('abcde')






