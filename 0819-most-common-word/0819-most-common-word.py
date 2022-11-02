class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sdict = dict()
        for s in re.split("[ |!|?|'|,|;|.]", paragraph):
            if s:
                astr = "".join(list(filter(str.isalpha, s.lower())))
                if astr not in banned:
                    if astr in list(sdict.keys()):
                        sdict[astr] = sdict[astr]+1
                    else:
                        sdict[astr] = 1
        return max(sdict, key=sdict.get)