# def romanToInt(s: str) -> int:
def romanToInt(s:str):
            mydict = {
                     'I' : 1,
                     'V' : 5, 'X' : 10,
                     'L' : 50, 'C' : 100,
                     'D' : 500, 'M' : 1000
                     }

            ans = 0

            for i in range(len(s)):
                if i < len(s) - 1 and mydict[s[i]] < mydict[s[i + 1]]:
                    ans -= mydict[s[i]]
                else:
                    ans += mydict[s[i]]

            print(ans)
            return ans


s = 'IXIII'
romanToInt(s)
