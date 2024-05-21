class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        curr=self.root
        for ch in word:
            if(ch not in curr.children):
                curr.children[ch]=TrieNode()
            curr=curr.children[ch]
            # curr.prefix+=1
        curr.end=True
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie=Trie()
        for word in strs:
            trie.insert(word)
        root=trie.root
        res=""
        for ch in strs[0]:
            # print(root,root.children,root.end)
            if(len(root.children)>1):
                return res
            if(root.end):
                break
            res+=ch
            
            root=root.children[ch]
        return res