class Solution:#https://velog.io/@jeongjae96/LeetCode-494-Target-Sum-%ED%8C%8C%EC%9D%B4%EC%8D%AC
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict() #(index, calculation result) -> number of ways which evaluate to target value
        # memo에 인덱스와 해당 인덱스까지의 계산 결과를 기록
        def backtrack(index, calc_result):
            if index == len(nums):
                return 1 if calc_result == target else 0
            if (index, calc_result) in memo:
                return memo[(index, calc_result)]
            memo[(index, calc_result)] = backtrack(index + 1, calc_result + nums[index]) + backtrack(index + 1, calc_result - nums[index])
            
            return memo[(index, calc_result)]
        return backtrack(0, 0)
        