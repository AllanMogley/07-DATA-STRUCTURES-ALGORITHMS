from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:

        le = min([len(strs[i]) for i in range(len(strs))])
        print(le)

        t = 0
        for j in strs:
            for x in j:
                while len(j) <= le and x == (y, l for y in j[t]):
                    print(x)
                    t += 1


myl = ['flow', 'flowe', 'flower']
ls = Solution
ls.longestCommonPrefix(myl)

   
