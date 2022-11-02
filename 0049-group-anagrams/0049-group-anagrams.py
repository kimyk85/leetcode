class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rstr = dict()
        for str in strs:
            # key = "".join(sorted(set(str)))
            key = "".join(sorted(list(str)))
            value = str
            # print(key, value)
            if key in rstr.keys():
                # templist = rstr[key]
                rstr[key].append(value)
            else:
                rstr[key] = [value]
        # print(rstr)

        rstr2 = list()
        for key, value in rstr.items():
            rstr2.append(value)
        return rstr2