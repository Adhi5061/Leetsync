class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        c=0
        for i in word:
            if(i==ch):
                break
            c+=1
        if(c>=len(word)):
            return word
        # print(c)
        return(word[c::-1]+word[c+1:])
        