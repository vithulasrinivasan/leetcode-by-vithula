class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        # print(type(binary)) # str
        prev=-1
        res=0
        for i in range(len(binary)):
            if binary[i]=='1':
                if prev!=-1:
                    res=max(res,i-prev)
                prev=i
        return res