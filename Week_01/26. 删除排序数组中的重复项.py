"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1 if nums else 0


if __name__ == '__main__':
    nums = [1, 3, 4, 6, 6, 7, 7]
    ret_class = Solution()
    print(ret_class.removeDuplicates(nums))
