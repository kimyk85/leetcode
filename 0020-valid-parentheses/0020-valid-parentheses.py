class Solution:
    def isValid(self, s: str) -> bool:
        Plist = list(s)
        Pdict = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for p in Plist:
            changedP = Pdict.get(p)
            if changedP:
                stack.append(changedP)
            else:
                if len(stack) == 0 or stack.pop(-1) != p:
                    return False
        if stack:
            return False
        return True