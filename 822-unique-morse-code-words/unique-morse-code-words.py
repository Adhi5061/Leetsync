class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        for i in words:
            con=""
            for j in i:
                val=ord(j)-97
                con+=morse[val]
            if(con in d):
                continue
            else:
                d[con]=1
        return(len(d))