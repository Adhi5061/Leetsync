class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        """for word in strs:
            for ind,ana in enumerate(res):
                if(sorted(word)==sorted(ana[0])):
                    res[ind].append(word)
                    break
            else:
                res.append([word])
        return res"""
        for word in strs:
            sortedw="".join(sorted(word))
            if(sortedw in res):
                res[sortedw].append(word)
            else:
                res[sortedw]=[word]
        return list(res.values())    