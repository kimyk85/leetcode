class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = dict()

        for v in jewels:
            j[v] = 0

        for s in stones:
            if s in j.keys():
                j[s] += 1

        total = 0
        for i, v in j.items():
            total = total + v
        return total