class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # freq = Counter({1:3, 2:2, 3:1})
        top_k_pairs = freq.most_common(k) # k=2 -> top_k_pairs = [(1,3), (2,2)]
        return [item for item, count in top_k_pairs] # Extract just the elements (ignore counts)
