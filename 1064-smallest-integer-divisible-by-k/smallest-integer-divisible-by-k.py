class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        #no num exists if k has factor 2 or 5
        if k%2==0 or k%5==0:
            return -1
        rem=1%k
        length=1
        while rem!=0:
            rem=(rem*10+1)%k
            length+=1
            #if length exceeds k, no solution
            if length>k:
                return -1
        return length