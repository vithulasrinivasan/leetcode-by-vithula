class Solution:
    def minFlips(self, s: str) -> int:
        '''
        Solution:-

        O(n**2):

        prefix of size s to the end - type 1 operation is free for us

        the alternating string of any size can be of 2 types: these are the targets for us:
        1) either it starts with 1 : 10101 (or)
        2) it starts with 0 : 01010

        compare the string with these targets and get the no of differences and get the no of operations to convert the string s to the idea alternating string , but we are not using the type 1 remove here

        O(n):

        for every prefix , move it to the end and then compare with our targets

        extend the target strings as we move the prefix to the end ! => reduce the repeating work

        add the string to itself

        '''

        n = len(s)
        s += s
        alt1 , alt2 = "" , ""

        for i in range(len(s)):
            alt1 += "0" if i%2 else "1"
            alt2 += "1" if i%2 else "0"

        res=len(s)
        diff1 , diff2 = 0,0 

        l=0 # sliding window left pointer
        for r in range(len(s)): # sliding window right pointer - every possible window
            if s[r]!=alt1[r]:
                diff1+=1

            if s[r]!=alt2[r]:
                diff2+=1

            if (r-l+1) > n:

                if s[l]!= alt1[l]:
                    diff1-=1
                if s[l]!= alt2[l]:
                    diff2-=1

                l+=1

            if (r-l+1)==n:
                res = min(res , diff1 , diff2)
            
        return res
        