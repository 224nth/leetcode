import string


class Solution:
    def isPalindrome(self, s: str) -> bool:

        i =0
        j = len(s) - i - 1
        while i <= len(s)//2:

            while i < len(s) and s[i] not in string.ascii_letters and s[i] not in string.digits:
                i +=1

            while j>= 0 and s[j] not in string.ascii_letters and s[j] not in string.digits:
                j -= 1

            if i >=j:
                break
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))