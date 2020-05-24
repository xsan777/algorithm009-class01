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
