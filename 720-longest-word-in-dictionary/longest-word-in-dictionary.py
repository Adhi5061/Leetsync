class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        l=len(word)
        curr=self.root
        for i in range(0,len(word)):
            if(word[i] not in curr.children):
                if(i+1!=l):
                    return 0
                else:
                    curr.children[word[i]]=TrieNode()
            curr=curr.children[word[i]]
        return l

class Solution:
    def longestWord(self, words: List[str]) -> str:
        res=""
        resl=0
        trie=Trie()
        curr=trie.root
        for word in sorted(words):
            l=trie.insert(word)
            if(l==resl):
                res=min(res,word)
            if(l>resl):
                resl=l
                res=word
        return res