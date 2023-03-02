class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) >= len(nums2):
            target = sorted(nums1)
            target2 = set(nums2)
        else:
            target = sorted(nums2)
            target2 = set(nums1)
        ra = []
        def search(s, t):
            if len(s) >= 1:
                i = len(s) // 2
                if s[i] < t:
                    return search(s[i+1:], t)
                elif s[i] > t:
                    return search(s[:i], t)
                elif s[i] == t:
                    return t

        for t in target2:
            rv = search(target, t)
            if rv is not None:
                ra.append(rv)
        return ra