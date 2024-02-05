# def romanToInt(s: str) -> int:
def romanToInt(s:str):
            mydict = {
                        'I' : 1,
                        'V' : 5, 'X' : 10,
                        'L' : 50, 'C' : 100,
                        'D' : 500, 'M' : 1000,

                        'IV' : 4, 'IX' : 9,
                        
                        'CD' : 400, 'CM' : 900}
            

            # mylist = mydict.get('L')
            ls = []
            for i in s:
                if i in mydict:
                    ls.append(i)
            print(ls)
            myls = [mydict.get(j) for j in ls]
            print(sum(myls))

            # mylist = [mydict.get(s) for x in range(len(s.split())) if s.split()[x] in mydict]
            # print(mylist)
            # return(sum(mylist))

s = 'IXIII'
romanToInt(s)
