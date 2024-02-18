class Solution:
    def __init__(self):
        self.d = {}

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if n in self.d:
            return self.d[n]
        elif n > 0:
            val1 = self.myPow(x, n // 2)
            val2 = self.myPow(x, n - (n // 2))
            val = val1 * val2
            self.d[n] = val
            return val
        else:
            val1 = self.myPow(x, n // 2)
            val2 = self.myPow(x, n - (n // 2))
            val = val1 * val2
            self.d[n] = val
            return val
