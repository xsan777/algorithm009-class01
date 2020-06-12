class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''递归，回溯解法'''
        ret = []
        n = len(nums)

        def helper(tmp, i):
            ret.append(tmp)
            for j in range(i, n):
                helper(tmp + [nums[j]], j + 1)
        helper([],0)
        return ret
