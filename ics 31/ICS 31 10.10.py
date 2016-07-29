#ICS 31, Thursday 10 October 2013

'''
if Statement:

print("What s the temperature?"
temp = int(input())

if temps<70:
    print("Wear a sweater"
else:
    print("Wear a T-shirt")
print("Have a comfortable day!")

Syntax:

if BOOLEANEXPRESSION:
      STATEMENTS)S)
else :
    STATEMENT(S)


Semantics:

If B.E. is true, do the statements after IF and skip statements after ELSE
If B.E. is false, slipe the statements after IF and do statements after ELSE

You can leave out the else part.

You can also ask compound questions:
Say we want a three-way distinction
    70 degrees and up: Wear a T-shirt
    50 to 69: Wear a sweater
    under 50: Wear a down jacket

print("What's the temperature?")
temp = int(input())

if temp>= 80:
    print("Wear a T-shirt")
if temp < 70 and temp >= 50:
    print("Wear a sweater")
if temp < 50:
    print("Wear a down jacket")
print("Have a comfortable day!")

def what_to_wear(temp: int)-> str:
    '''Return 'T-shirt', 'sweater', 'down jacket' depending on temperature '''
    if temp>=70:
        result ='T-shirt'
        if temp < 70 and temp >=50:
            result = 'sweater'
        if temp < 50:
            result ='down jacket'
        return result

print("what's the temperature?")
temp = int(input())
print("Wear a ", what_to_wear(temp), '.')
print("Have a nice day.")

assert what_to_wear(55) == 'sweater'
assert what_to_wear(75) == 'T-shirt'
assert what_to_wear(105) == 'T-shirt'
assert what_to_wear(30) == 'down jacket'
assert what_to_wear(-25) == 'down jacket'
assert what_to_wear(50) == 'sweater'
assert what_to_wear(49) == 'down jacket'
assert what_to_wear(51) == 'down jacket'
assert what_to_wear(69) =='sweater'
assert what_to_wear(70) == 'T-shirt'
assert what_to_wear(71) == 'T-shirt'

One form of repition: A for-loop for a sequence.
'''

L = [234,34234,3245,24535345, 34535, 58, 9088]
print(L)

print(L[0])
print(L[1])
print(L[2])
print(L[3])

print('=============')
for item in L:
    print(item)

Syntax:

for VariableNAME in Sequence:
    STATMENT(S) == BODY OF THE LOOP

Semantics:
    First the variable refers to the first item in the sequence.
        Then do the body of the loop.
        Next the variable refers to the second item
            Then do the body of the loop again, with the variable pointing to #2
        Keep going until the end of the sequene
