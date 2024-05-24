from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def possible(word,lis):
            w=dict(Counter(word))
            l=dict(Counter(lis))
            for key,val in w.items():
                if(key not in l):
                    return False
                if(l[key]<w[key]):
                    return False
            return True

        def bt(pos,lts):
            if(pos==len(words)):
                return 0
            word=words[pos]
            if(possible(word,lts)):
                l=list(word)
                cres=0
                for char in l:
                    cres+=score[ord(char)-97]
                    lts.remove(char)
                f=bt(pos+1,lts)
                for char in l:
                    lts.append(char)
                se=bt(pos+1,lts)
                return max(cres+f,se)
            return bt(pos+1,lts)

        return bt(0,letters)
