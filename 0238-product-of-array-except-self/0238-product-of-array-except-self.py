class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = []
        left = 1
        right = 1
        left_list = []
        right_list = []

        for i in range(len(nums) -1 , 0,  -1):
            right = right * nums[i]
            right_list.append(right)
        right_list.reverse()
        right_list.append(1)

        return_list.append(right_list[0])
        for i in range(0, len(nums)-1):
            left = left * nums[i]
            left_list.append(left)
            return_list.append(left * right_list[i+1])
        return return_list