class Solution:
    def bestClosingTime(self, customers: str) -> int:
        minpenalty , curpenalty , earliesthr = 0, 0, 0
        for i in range(len(customers)):
            ch = customers[i]
            if ch=='Y':
                curpenalty-=1
            else:
                curpenalty+=1
            if curpenalty<minpenalty:
                earliesthr= i+1
                minpenalty = curpenalty
        return earliesthr