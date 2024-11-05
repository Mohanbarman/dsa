import math


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        i = 0
        x_abs = abs(x)

        while x_abs > 0:
            res *= 10
            res += x_abs % 10
            if res > 2**31:
                return 0
            x_abs //= 10
            i += 1

        if x < 0:
            return res * -1

        return res

    def reverse2(self, x: int) -> int:
        INT_MAX_L = 214748364
        INT_MAX_R = 7
        INT_MIN_L = -214748364
        INT_MIN_R = -8

        res = 0

        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (res > INT_MAX_L) or (res == INT_MAX_L and digit > INT_MAX_R):
                return 0
            if (res < INT_MIN_L) or (res == INT_MAX_L and digit < INT_MIN_R):
                return 0

            res = (res * 10) + digit

        return res


# print(Solution().reverse2(123))
print(Solution().reverse2(1534236469))
