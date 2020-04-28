class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        coins.sort(reverse=True)

        return self.__coin_change(0, coins, amount, 0)

    def __coin_change(self, index, coins, amount, step):

        if amount < 0:
            return -1
        elif amount == 0:
            return step

        for i in range(index, len(coins)):
            res = self.__coin_change(index, coins, amount - coins[i], step+1)
            if res >= 0:
                return res

        return -1


coins = [1, 2, 5]
amount = 11
assert (Solution().coinChange(coins, amount) == 3)


coins=[2]
amount = 3
assert (Solution().coinChange(coins, amount) == -1)
