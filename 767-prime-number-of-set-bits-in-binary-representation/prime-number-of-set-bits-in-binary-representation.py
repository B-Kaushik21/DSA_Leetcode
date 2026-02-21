class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        def helper(num):
            count=0
            for n in num:
                if n=='1':
                    count+=1
            return count

        def is_prime(n):
            if n < 2:
                return False

            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False

            for i in range(2, int(n**0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, n + 1, i):
                        sieve[j] = False

            return sieve[n]
        
        for i in range(left,right+1):
            if is_prime(helper(bin(i)[2:])):
                res+=1
        return res