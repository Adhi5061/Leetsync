class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source=set()
        des=set()
        for i in paths:
            source.add(i[0])
            des.add(i[1])
        return((des-source).pop())