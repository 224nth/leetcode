from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans =[]
        nums.sort()

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            s = i+1
            l = len(nums)-1



            while s < l:
                b= nums[s]
                c =nums[l]

                if a+b+c == 0:
                    ans.append([a,b,c])
                    l-=1
                    s+=1

                    while s <l and nums[s] == nums[s-1]:
                        s += 1
                    while s<l and nums[l] == nums[l+1]:
                        l -=1

                elif a+b+c > 0:
                    l -= 1
                else:
                    s += 1

        return ans

num =[-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(num))