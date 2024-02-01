from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        print(d)
        mc=[element for element,count in d.most_common(k)]
        return mc