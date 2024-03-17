class Test:
    def prefix(self, s: str) -> str:

        ans = ''
        for i in range(len(s)):
            while s[i] not in ans:
                ans += s[i]
        print('None ', ans)


strs = Test()
text = 'pwwkew'
print(strs.prefix(text))
