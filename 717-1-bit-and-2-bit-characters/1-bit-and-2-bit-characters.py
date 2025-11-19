class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n=len(bits)
        i=0
        while i<n-1:
            if bits[i]==1:
                i=i+2
            else:
                i=i+1
        return True if i!=n else False