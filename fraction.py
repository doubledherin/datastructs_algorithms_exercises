class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, other):
        newFracNum = self.num * other.den + other.num * self.den
        newFracDen = self.den * other.den
        
        common = gcd(newFracNum, newFracDen)

        newFrac = Fraction(newFracNum//common, newFracDen//common)
        return str(newFrac)

    def __eq__(self, other):
        first = self.num * other.den
        second = other.num * self.den
        return first == second 

def gcd(num1, num2):

    while num1 % num2 != 0:
        oldnum1 = num1
        oldnum2 = num2

        num1 = oldnum2
        num2 = oldnum1 % oldnum2

    return num2