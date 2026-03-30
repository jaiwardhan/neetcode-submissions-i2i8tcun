class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_lookup = {}
        for n in nums:
            if n not in count_lookup:
                count_lookup[n] = 0
            count_lookup[n] += 1
        l = [(a, count_lookup[a]) for a in count_lookup.keys()]
        l.sort(key=lambda a: a[1])
        return [a[0] for a in l[-k:]]