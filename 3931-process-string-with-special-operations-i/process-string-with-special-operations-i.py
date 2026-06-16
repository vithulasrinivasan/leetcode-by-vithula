class Solution:
    def processStr(self, s: str) -> str:
        
        res=[]
        for c in s:
            if c.islower():
                res.append(c)
            elif c == '*':
                if res:
                    res.pop()
            elif c=='#':
                res+=res
            elif c=='%':
                res.reverse()

        return "".join(res)