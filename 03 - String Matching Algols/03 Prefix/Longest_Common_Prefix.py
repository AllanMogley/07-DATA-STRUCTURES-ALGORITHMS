from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:

        le = min([len(strs[i]) for i in range(len(strs))])
        print(le)
        
        ans = ''
        first = strs[0]
        last = strs[-1]

        for i in range (le):
            if first[i] != last[i]:
                print('None')
            ans += first[i]
            print(ans)


myl = ['flow', 'flowe', 'flower']
ls = Solution
ls.longestCommonPrefix(myl)

   
