

def romanToInt(s:str):
            
            #-------------------------------------------------------------------
            # Create dictionary to hold Key and Values
            #-------------------------------------------------------------------
            mydict = {
                     'I' : 1,
                     'V' : 5, 'X' : 10,
                     'L' : 50, 'C' : 100,
                     'D' : 500, 'M' : 1000
                     }


            #-------------------------------------------------------------------
            # Loop through the string and check and compare value in dictionary
            #-------------------------------------------------------------------
            ans = 0
            print('String Length ---> ', len(s))
            for i in range(len(s)):
                if i < len(s) - 1 and mydict[s[i]] < mydict[s[i + 1]]:
                    ans -= mydict[s[i]]
                else:
                    ans += mydict[s[i]]
            
            print('\n')
            print('Roman Value ------->', s)
            print('Numerical Value ---> ', ans)
            print('\n')
            return ans


s = "MCMXCIV"
romanToInt(s)


