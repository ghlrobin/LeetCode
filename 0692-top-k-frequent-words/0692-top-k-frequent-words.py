from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        topk = Counter(words).most_common()
        topk = sorted(topk, key = lambda x : (-x[1], x[0]))
        topk = topk[:k]
        return [x for x, y in topk]
        