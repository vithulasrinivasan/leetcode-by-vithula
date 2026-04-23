class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = defaultdict(list)

        for i, num in enumerate(nums):
            mp[num].append(i)


        n = len(nums)
        arr = [0] * n

        for lst in mp.values():

            size = len(lst)

            prefix = [0] * size
            prefix[0] = lst[0]

            for i in range(1, size):
                prefix[i] = prefix[i-1] + lst[i]

            for i in range(size):

                idx = lst [i]

                sum_left = prefix[i-1] if i>0 else 0
                sum_right = prefix[-1] - prefix[i]

                count_left = i
                count_right = size-i-1

                left = idx * count_left - sum_left
                right = sum_right - idx * count_right

                arr[idx] = left + right
        
        return arr