from typing import List

class Solution:
    def longestCommonPrefix(strs: List[str]) -> str:

        le = min([len(strs[i]) for i in range(len(strs))])
        print(le)

        t = 0
        for j in strs:
            a = [x for x in strs[0]]
            b = [q for q in strs[1]]
            c = [z for z in strs[2]]

        for f in a:
            for g in b:
                for h in c:
                    while f == g == h:
                        print(f)

     

            # while a == q:
        print('a', a)
        print('b', b)
        print('c', c)
            # t += 1


myl = ['flow', 'flowe', 'flower']
ls = Solution
ls.longestCommonPrefix(myl)

   
