# Created by Jula at 2026/08/05 11:55
# leetgo: 1.4.17
# https://leetcode.com/problems/palindrome-number/

from typing import *
from leetgo_py import *
import math

# @lc code=begin

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            length = int(math.log10(x)) + 1
            while length > 1:
                first = int(x / 10 ** (length - 1))
                last = x % 10

                if first != last:
                    return False

                x -= first * 10 ** (length - 1)
                x //= 10
                length -= 2

        return True

        # return str(x) == str(x)[::-1]



# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    ans = Solution().isPalindrome(x)
    print("\noutput:", serialize(ans, "boolean"))
