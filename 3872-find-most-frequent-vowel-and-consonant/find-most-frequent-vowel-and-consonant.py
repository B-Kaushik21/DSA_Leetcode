class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowFreq,constFreq={},{}
        maxVowel,maxConst=float('-inf'),float('-inf')
        for char in s:
            if char in 'aeiou':
                if char not in vowFreq:
                    vowFreq[char]=1
                else:
                    vowFreq[char]+=1
            else:
                if char not in constFreq:
                    constFreq[char]=1
                else:
                    constFreq[char]+=1

        for key,val in vowFreq.items():
            maxVowel=max(maxVowel,val)
        for key,val in constFreq.items():
            maxConst=max(maxConst,val)

        if len(vowFreq)==0:
            return maxConst
        if len(constFreq)==0:
            return maxVowel
            
        return maxVowel+maxConst
