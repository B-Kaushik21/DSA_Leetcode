class Solution:
    def passwordStrength(self, password: str) -> int:
        lower='abcdefghijklmnopqrstuvwxyz'
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits='0123456789'
        spl='!@#$'

        pwd=''
        for p in password:
            if p not in pwd:
                pwd+=p
        #print(pwd)
        ans=0
        for p in pwd:
            if p in lower:
                ans+=1
            elif p in upper:
                ans+=2
            elif p in digits:
                ans+=3
            else:
                ans+=5
        return ans