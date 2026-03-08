class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        def gen(curr):
            if len(curr)==n:
                if curr not in nums:
                    return curr
                return ""
            add_Zero=gen(curr+"0")
            if add_Zero:
                return add_Zero
            return gen(curr+"1")
        n=len(nums)
        nums=set(nums)
        return gen("")