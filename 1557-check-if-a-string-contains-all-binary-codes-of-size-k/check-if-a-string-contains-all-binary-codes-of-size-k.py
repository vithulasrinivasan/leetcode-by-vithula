class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
        no of binary code of length k = 2^k
        '''
        codeset=set()
        for i in range(len(s)-k+1):
            codeset.add(s[i:i+k])
        return len(codeset)==2**k