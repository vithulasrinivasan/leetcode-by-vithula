class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # 1950 to 2050 = 101 years

        people_count = [0] * 101

        for birth,death in logs:
            people_count[birth - 1950] += 1
            people_count[death - 1950] -= 1

        for i in range(1,101):
            people_count[i] += people_count[i-1]

        return people_count.index(max(people_count)) + 1950
