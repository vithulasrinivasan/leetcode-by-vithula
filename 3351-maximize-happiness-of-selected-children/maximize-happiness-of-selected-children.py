class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        n=len(happiness)
        if k>n:
            k=n
        selected=happiness.pop()
        
        for i in range(1,k):
            now = happiness.pop() - i
            if now<=0:
                break
            selected+= now
            
        return selected
            
        