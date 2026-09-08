class Solution:
    def countCommas(self, n: int) -> int:

        #Angel

        if n < 1000:
            return 0

        if n < 100000:
            return n - 999

        return 99001