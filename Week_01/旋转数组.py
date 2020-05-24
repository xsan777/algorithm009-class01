class Solution:
    # 循环插入法
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            nums.insert(0,nums.pop())
            i += 1
        return nums
    # 最优法：三次反转法、切片法
    def rotate_2(self,nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
        return nums


if __name__ == '__main__':
    nums = [1,5,8,7,8,6,8,4]
    # nums = []
    k = 2
    print(Solution().rotate_2(nums,k))