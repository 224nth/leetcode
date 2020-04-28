from functools import cmp_to_key


class Solution(object):

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        print(nums)
        def mysorter(a, b):
            return int(b+a)-int(a+b)

        str_nums = [str(x) for x in nums]

        str_nums.sort(key=cmp_to_key(mysorter))
        print(str_nums)
        return ''.join(str_nums)

arr = [3,30,34,5,9]
print(Solution().largestNumber(arr) )
assert (Solution().largestNumber(arr) == '9534330')