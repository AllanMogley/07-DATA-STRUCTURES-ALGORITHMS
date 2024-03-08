class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return[]

alg = Solution
ls = [3, 2, 3, 5, 9, 10]
t = 6
print(alg.twoSum(ls,t))


