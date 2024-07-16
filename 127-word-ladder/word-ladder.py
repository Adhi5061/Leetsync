class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        q=deque()
        t=1
        wordList=set(wordList)
        if(beginWord in wordList):
            wordList.remove(beginWord)
        q.append((beginWord,1))
        visited=set()
        while(q):
            word,l=q.popleft()
            if(len(visited)==len(wordList)):
                return 0
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    wordl=word[:i]+char+word[i+1:]
                    if(wordl in wordList):
                        if(wordl in visited):
                            continue
                        if(wordl==endWord):
                            return l+1
                        visited.add(wordl)
                        q.append((wordl,l+1))
        return 0