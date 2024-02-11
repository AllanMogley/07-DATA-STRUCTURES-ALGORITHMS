from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str

        t = 0
        for j in strs:
            for x in j:
                while x == j[t]:
                    print(x)
                    t += 1


myl = ['flow', 'flowe', 'flower']
ls = Solution
ls.longestCommonPrefix(myl)

   
