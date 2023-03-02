class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = bisect.bisect_right(numbers, target)
        left = 0
        right = len(numbers)-1 if index >= len(numbers) or index == 0 else index
        while left < right:
            sumv = numbers[left] + numbers[right]
            if sumv == target:
                return [left+1, right+1]
            elif sumv > target:
                right -= 1
            else:
                left += 1