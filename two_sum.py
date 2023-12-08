from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f"Nums: {nums}, Target: {target}")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                print(f"I: {nums[i]}, J: {nums[j]} = {nums[i]+nums[j]}")
                if nums[i]+nums[j] == target:
                    return [i,j]

#main
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([3,2,4], 6))