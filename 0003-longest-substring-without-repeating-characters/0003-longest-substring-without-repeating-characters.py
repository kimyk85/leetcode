class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = dict()
        maxlen = 0
        for i, v in enumerate(s):
            j = i + 1
            ans[v] = 1
            while j < len(s):
                if ans.get(s[j]):
                    maxlen = (len(ans) if maxlen < len(ans) else maxlen)
                    ans.clear()
                    # ans[v] = 1
                    break
                else:
                    ans[s[j]] = 1
                j += 1
        maxlen = (len(ans) if maxlen < len(ans) else maxlen)
        return maxlen
        