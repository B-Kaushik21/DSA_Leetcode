class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words=[]
        temp=""
        for i in range(len(title)):
            if title[i]!=" ":
                temp+=title[i]
            else:
                words.append(temp)
                temp=""
        words.append(temp)
        #print(words)
        for w in range(len(words)):
            n=len(words[w])
            if n<=2:
                words[w]=words[w].lower() 
            else:
                words[w]=words[w].capitalize()
        return ' '.join(words)