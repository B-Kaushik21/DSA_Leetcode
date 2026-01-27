class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (int(num1[i])) * (int(num2[j]))
                p1 = i + j
                p2 = i + j + 1
                summ = mul + pos[p2]
                pos[p1] += summ // 10
                pos[p2] = summ % 10
        sb = ''
        for p in pos:
            if not (len(sb) == 0 and p == 0):  # Skip leading zeros
                sb += str(p)
        
        return sb if sb else "0"