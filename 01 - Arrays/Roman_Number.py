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
            print('List 1 = ',ls)


            ch = ['I', 'X']
            if ch[0:1] == ls[0:1]:
                for t in ch:
                    if t in ls:
                        ls.pop(0)
                ls.insert(0,'IX')
                print('List 2 = ', ls)
            myls = [mydict.get(j) for j in ls]
            print(sum(myls))


s = 'XIII'
romanToInt(s)
