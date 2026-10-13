"""
claude
Don't generate lab for this
"""

class RationalNumber:
    def __init__(self, p, q):
        self.numerator = p
        self.denominator = q

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            result_numerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)
            result_denominator = self.denominator * other.denominator
            return RationalNumber(result_numerator, result_denominator)
        else:
            return self

    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            result_numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
            result_denominator = self.denominator * other.denominator
            return RationalNumber(result_numerator, result_denominator)
        else:
            return self

    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            result_numerator = self.numerator * other.numerator
            result_denominator = self.denominator * other.denominator
            return RationalNumber(result_numerator, result_denominator)
        else:
            return self

    def __lt__(self, other):
        if isinstance(other, RationalNumber):
            result_numerator = self.numerator * other.denominator
            result_denominator = self.denominator * other.numerator
            return result_numerator < result_denominator
        else:
            return False

    def __repr__(self) -> str: return str(self.numerator) + '/' + str(self.denominator)

rational1 = RationalNumber(1,2)
rational2 = RationalNumber(1,2)
print(rational1 + rational2)
print(rational1 - rational2)
print(rational1 * rational2)
print(rational1 < rational2)