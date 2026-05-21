class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        premap=defaultdict(int)
        for num in arr1:
            str_num=str(num)
            pre=''
            for i in str_num:
                pre+=i
                premap[pre]+=1
        ans=0
        for num in arr2:
            str_num=str(num)
            pre=''
            for i in str_num:
                pre+=i
                if pre in premap:
                    ans=max(ans,len(pre))
        return ans
        