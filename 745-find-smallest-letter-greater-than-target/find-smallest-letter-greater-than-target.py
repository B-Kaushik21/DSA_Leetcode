class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res=[0]*len(letters)
        for l in range(len(letters)):
            res[l]=ord(letters[l])-ord(target)
        print(res)

        for i in range(len(letters)):
            if res[i]>0:
                return letters[i]
        return letters[0]
        
