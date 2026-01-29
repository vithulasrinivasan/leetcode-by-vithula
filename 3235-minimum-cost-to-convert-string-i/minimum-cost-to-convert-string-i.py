class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        c=[[float('inf')]*26 for i in range(26)]
        for i in range(26):
            c[i][i]=0
        def o(a):
            return ord(a)-ord('a')

        for a,b,k in zip(original,changed,cost):
            c[o(a)][o(b)]=min(c[o(a)][o(b)],k)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    c[i][j]=min(c[i][j], c[i][k]+c[k][j])
        
        min_cost=0
        for a,b in zip(source,target):
            if c[o(a)][o(b)]==float('inf'):
                return -1
            min_cost+=c[o(a)][o(b)]
        return min_cost