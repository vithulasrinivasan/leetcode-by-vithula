class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot_apples=sum(apple)
        capacity.sort(reverse=True)    
        for idx, cap in enumerate(capacity):
            tot_apples -= cap
            if tot_apples <= 0:
                return idx + 1