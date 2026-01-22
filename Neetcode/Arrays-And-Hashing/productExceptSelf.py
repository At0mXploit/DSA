class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        n = len(nums)                 # n = 4
        output = [1] * n              # output = [1, 1, 1, 1]

        # PREFIX PASS
        prefix = 1

        # i = 0
        # output[0] = prefix = 1
        # prefix = prefix * nums[0] = 1 * 1 = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # After prefix loop:
        # output = [1, 1, 2, 8]
        #prefix = 48 (not used further)

        # SUFFIX PASS
        suffix = 1

        # i = 3
        # output[3] = 8 * 1 = 8
        # suffix = suffix * nums[3] = 1 * 6 = 6

        # i = 2
        # output[2] = 2 * 6 = 12
        # suffix = 6 * 4 = 24

        # i = 1
        # output[1] = 1 * 24 = 24
        # suffix = 24 * 2 = 48

        # i = 0
        # output[0] = 1 * 48 = 48
        # suffix = 48 * 1 = 48
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        # Final output = [48, 24, 12, 8]
        return output

