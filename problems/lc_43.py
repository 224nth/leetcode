class Solution:

    def multiply_single(self, nums, a):

        carry = 0

        result = ""
        for number in nums[::-1]:
            temp = int(number) * int(a) + carry
            if temp > 9:
                carry = int(temp/10)
            else:
                carry = 0

            result = str(int(temp%10))+ str(result)
        if carry > 0:
            result = str(carry) +result
        return result


    def multiply(self, num1: str, num2: str) -> str:

        result = 0
        for i in num2:
            result += result*10 + int(self.multiply_single(num1, i))
            print('1')


        return str(int(result))


print(Solution().multiply('123','456'))


