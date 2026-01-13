class Solution:
    def validStrings(self, n: int) -> List[str]:
        valid=['0','1']
        if n==1:
            return valid

        for i in range(n-1):
            new_valid=[]
            for s in valid:
                if s[-1]=='1':
                    new_valid.append(s+'1')
                    new_valid.append(s+'0')
                else:
                    new_valid.append(s+'1')
            valid=new_valid
        return valid
