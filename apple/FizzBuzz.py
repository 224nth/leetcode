

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        res = [str(i+1) for i in range(n)]

        cnt = 2
        while cnt < n:
            res[cnt] = "Fizz"
            cnt += 3

        cnt = 4
        while cnt < n:
            res[cnt] = "Buzz" if res[cnt] != "Fizz" else res[cnt] + "Buzz"
            cnt += 5

        return res


assert Solution().fizzBuzz(15) == [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]