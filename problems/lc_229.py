from typing import  List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        cnt1, cnt2 = 0 ,0
        num1, num2 = None, None

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                num1 = num
                cnt1 =1
            elif cnt2 == 0:
                cnt2 =1
                num2 = num
            else:
                cnt1 -=1
                cnt2 -=1

        res = []
        if nums.count(num1) > len(nums)/3:
            res.append(num1)
        if nums.count(num2) > len(nums)/3:
            res.append(num2)

        if len(res) == 1:
            return res[0]
        return res


#assert Solution().majorityElement([3,2,3]) == 3
assert Solution().majorityElement([1,1,1,3,3,2,2,2]) == [1,2]