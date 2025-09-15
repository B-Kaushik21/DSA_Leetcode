class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        brokenKeys=set(brokenLetters)
        words=text.split(" ")
        for word in words:
            for c in word:
                if c in brokenKeys:
                    count+=1
                    break
        return len(words)-count