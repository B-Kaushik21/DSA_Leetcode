class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid=[]
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        n=len(code)
        for i in range(n):
            if isActive[i]:
                if re.match('^[a-zA-Z0-9_]+$',code[i]):
                    if businessLine[i] in ['electronics','grocery','pharmacy','restaurant']: 
                        valid.append((order[businessLine[i]], code[i]))
        valid.sort()
        return [c for _,c in valid]