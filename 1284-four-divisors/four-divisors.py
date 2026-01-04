class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        '''
        --> Key Idea:
        A number has exactly 4 divisors only if it is:

        The cube of a prime (p³) → divisors = {1, p, p², p³}

        The product of two distinct primes (p × q) → divisors = {1, p, q, p*q}.

        --> Algorithm:

        For each number n in nums:

        Check if n is a perfect cube and its cube root is prime → return 1 + p + p² + p³.

        Otherwise, try dividing n by integers up to √n.

        If you find a factorization n = p × q with both p and q primes (and distinct), return 1 + p + q + n.

        Else return 0.

        Add up results for all numbers.
        '''
        import math

        def is_prime(x):
            if x<2:
                return False
            for i in range(2,int(math.sqrt(x))+1):
                if x%i==0:
                    return False
            return True

        total_sum=0

        for n in nums:
            #case 1: n=p^3
            p=round(n**(1/3)) #cube root of n = p
            if p**3==n and is_prime(p):
                total_sum += 1 + p + p*p + n
                continue
            
            #case 2: n=p*q where p!=q and both primes
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    j=n//i
                    if i!=j and is_prime(i) and is_prime(j):
                        total_sum += 1 + i + j + n
                        break

        return total_sum