''' Sieve of Eratosthenes '''

maxv = 1000001
pf = [i for i in range(maxv)] # list of positive numbers starting from 0 to maxv
pf [0] = 0
pf [1] = 1
i=2

while i*i < maxv: # prime factor criteria , sqaure root of n
    if pf[i] == i: # 2==2
        j=i*i # j=4
        while j<maxv: # j<maxv -> true
            if pf[j]==j: #4==4 yes
                pf[j] = i # multiple of i #pf[4]=2
            j+=i # next multiple of i # j = 4+2 = 6
    
    i+=1 

class Solution:
    def isPrime(self,x):
        return x>=2 and pf[x]==x

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0

        maxi=max(nums)

        primeinnums = [False] * (maxi + 1) # primes actually present in given nums

        for x in nums:
            if self.isPrime(x):
                primeinnums[x]=True

        mp = defaultdict(list) # prime p -> divisible indices j , ie nums[j]%p==0

        for i,val in enumerate(nums):
            if val == 1:
                continue
            x=val
            while x>1:
                p=pf[x]
                if p<= maxi and primeinnums[p]:
                    mp[p].append(i)

                while x%p==0:
                    x//=p

        dist = [-1]*n
        dist[0]=0

        usedPrime = [False] * (maxi+1)
        q=deque([0])

        while q:
            idx = q.popleft()
            if idx==n-1:
                return dist[idx]

            d = dist[idx] + 1

            if idx-1 >=0 and dist[idx-1] == -1: # left
                dist[idx-1] = d
                q.append(idx-1)

            if idx+1 < n and dist[idx+1]== -1: # right
                dist[idx+1] = d
                q.append(idx+1)

            x = nums[idx]

            if self.isPrime(x) and not usedPrime[x]: #teleportation
                usedPrime[x]=True
                for nxtidx in mp[x]:
                    if dist[nxtidx] == -1:
                        dist[nxtidx] = d
                        q.append(nxtidx)

        return -1


        
        
