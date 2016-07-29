#Create 4 classes for
#the 4 operations + = * /
#always add/multiply/subtract/divide by 10
#Ask a user what they want
#Perform the operation on a number

class Add:
    def math(self, n: float)-> float:
        return n+10
class Subtract:
    def math(self, n: float)-> float:
        return n-10

class Multiply:
    def math(self, n: float)-> float:
        return n*10

class Divide:
    def math(self, n: float)-> float:
        return n/10

u_i = input("Choose an operation: ")

if u_i == 'a':
    algebra = Add()

elif u_i == 's':
    algebra = Subtract()

elif u_i == 'm':
    algebra = Multiply()

elif u_i == 'd':
    algebra = Divide()

n = int(input("Choose a number: "))
print(algebra.math(n))
        
