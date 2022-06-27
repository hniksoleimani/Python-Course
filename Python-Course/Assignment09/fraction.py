class Fraction:
    def __init__(self,num, den):
        self.numerator = num 
        self.denominator = den  

    def sum(self, mehman):
        result = Fraction(None, None)
        result.numerator = self.numerator * mehman.denominator + self.denominator * mehman.numerator 
        result.denominator = self.denominator * mehman.denominator
        return result
        
    def multiply(self, mehman):
        result = Fraction(None, None)
        result.numerator = self.numerator * mehman.numerator
        result.denominator = self.denominator * mehman.denominator
        return result
    def sub(self, mehman):
        result = Fraction(None, None)
        result.numerator = self.numerator * mehman.denominator - self.denominator * mehman.numerator 
        result.denominator = self.denominator * mehman.denominator
        return result


    def div(self, mehman):
        result = Fraction(None, None)
        result.numerator = self.numerator * mehman.denominator
        result.denominator = self.denominator * mehman.numerator
        return(result)


    def show(self):
        print(self.numerator, '/', self.denominator)


a = Fraction(1, 2)
b = Fraction(1,3)
a.show()
b.show()
c = a.sub(b)
c.show()