class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = dict(Counter(stones))
        total = 0
        for j in jewels:
            if j in s.keys():
                total = total + s[j]
        return total