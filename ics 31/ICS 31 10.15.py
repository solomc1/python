hours1= 25
hours2 = 45
rate = 10

print ("Salary fo", 25, "hours should be", hours1 * rate)
print("Salary for", 45, "hours should be", 40 * rate + 5 * (rate *1.5))

from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
R1 = Restaurant("Tour d'Argent", 'French', '01-22-33-44-66,''Escargots', 34.50)
print (R1)
#R1.name = "Joe's"
# Namedtuples are IMMUTABLE -- can't change them in place.
#Change a field by creating a new item with (mostly) old values
R1 = Restaurant ("Joe's", R1.cuisine, R1.phone, R1.dish, R1.price)
print (R1)
# Change a field using the _replace method:
R1._replace(name="Sam's", price=100)
print(R1)
            
#Lists, though, are MUTABLE
L = ['Huey', 'Dewey', 'Louie']
print(L)
L[2] = 'Donald'
print(L)
