import itertools
from itertools import repeat


class Snow:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, n):
        return self.amount + n

    def __sub__(self, n):
        return self.amount - n

    def __mul__(self, n):
        return self.amount * n

    def __truediv__(self, n):
        return self.amount // n

    def makeSnow(self, amount_in_row: int) -> str:
        result = ''.join(["*" * amount_in_row, "/n"])
        finish_res = (result * self.amount)[:-2]
        return finish_res


snow1 = Snow(5)
print(snow1.makeSnow(10))

