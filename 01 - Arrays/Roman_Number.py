def romanToInt(s: str) -> int:
            mydict = {
                        'I' : 1, 'II' : 2, 'III' : 3,
                        'V' : 5, 'X' : 10,
                        'L' : 50, 'C' : 100,
                        'D' : 500, 'M' : 1000,

                        'IV' : 4, 'IX' : 9,
                        'XL' : 40, 'XC' : 90,
                        'CD' : 400, 'CM' : 900}
                                                                                                                    
            mylist = [mydict.get(x) for x in range(len(s.split())) if s.split()[x] == mydict]
            print(sum(mylist))
            return(sum(mylist))
s = 'LV'
romanToInt(s)
