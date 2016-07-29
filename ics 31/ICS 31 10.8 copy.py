def double(x):
    return 2*x

print(double(8), 'should be 16')
print(double(0), 'should be zero')
print(double(2+3+double(0)) + double(10), 'should be 30')

def print_ten_stars():
    print("**********")
    return

print_ten_stars()

def print_n_stars(n):
    pirint(n * '*')
    return

print_n_stars(5)
print("Above should be *****")
print_n_stars(10)           
print('Aboeve should be ********')

def ten_stars():
    return"************"

print(ten_stars())
print("Above should be **********, 10 stars")
print(ten_stars() =="**********")

def n_stars(n):
    return n * '*'

print(n_stars(10))
print("Above should be ***********, 10 stars")
print(n_stars(5) == "******")

def n_copies(n, s):
         return n* s

print(n_copies(10, '*'))
print("Above should be 10 stars")
print(n_copies(5, 'ok'))
print('above should be "okokokookok"')
         
def n_copies2(n: int, s: str) -> str :
    " Return n copies of the sting s "
    return n * s

assert n_copies2(5, '*') == "*****"
assert n_copies2(6, 'ok') == "okokokokokok"
assert n_copies2(0, 'Hello') ===
