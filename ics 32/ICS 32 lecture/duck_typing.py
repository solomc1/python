# squraing a number

def square(n:'number')->int:
    return n*n

#a kind of object that knows how to square a number

class SquareCalculation:
    def calculate(self, n):
        return n*n

class LengthCalculation:
    def calculate(self,n):
        return len(n)

class SquareRootcalculation:
    def calculate(self, n):
        return math.sqrt(n)

def run_calculations(calculations: 'list of Calculations', starting_value:'some value'):
    current_value = starting_value

    for calcution in calculations:
        current_value = calculation.calculate(current_value)

    return current_value

