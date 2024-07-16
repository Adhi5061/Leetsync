class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        q=deque()
        t=1
        wordList=set(wordList)
        if(beginWord in wordList):
            wordList.remove(beginWord)
            t+=1
        q.append((beginWord,1))
        visited=set()
        while(q):
            word,l=q.popleft()
            # print(word,l,visited)
            if(len(visited)==len(wordList)):
                return 0
            for wordl in wordList:
                if(wordl in visited):
                    continue
                if(len(wordl)==len(word)):
                    res=0
                    for i in range(len(word)):
                        res+=1 if(word[i]!=wordl[i]) else 0
                    # print(wordl,word,res)
                    if(res==1):
                        if(wordl==endWord):
                            return l+1
                        visited.add(wordl)
                        # print(elist)
                        # print(word,wordl,l+1)
                        q.append((wordl,l+1))
        return 0