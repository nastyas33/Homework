import math

def nok (num1: int, num2: int) -> float:
    import math
    multiple = math.lcm(num1, num2)
    return multiple

print (nok(num1=14, num2=30))

#второе решение
def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

def mcd(n, m):
    return (n/gcd(n, m)) * m

print(mcd(14, 30))