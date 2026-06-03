class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        inf = 10 ** 20 

        def f(landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]):
            best , landends = inf, inf 

            for s, d in zip(landStartTime, landDuration):
                landends = min(landends, s+d) 
                # one land ride that ends the earliest first

            for s,d in zip(waterStartTime, waterDuration):
                if s>= landends:
                    best = min(best, s+d)

                else:
                    best = min(best, landends+d)

            return best 

        return min(f(landStartTime, landDuration, waterStartTime, waterDuration), f(waterStartTime, waterDuration, landStartTime, landDuration) )