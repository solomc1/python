#Create 4 animal classes that have functions growl and eat
#Ask a user which animal they want and make it growl and eat

class Zebra:
    def growl(self)->str:
        print("I'm eating grass...")

class Giraffe:
    def growl(self)->str:
        print("I'm eating cupcakes...")
        
class Moose:
    def growl(self)->str:
        print("I'm eating pho")

class Tiger:
    def growl(self)->str:
        print("I'm eating you...")

u_i = input("Choose an animal: ").lower()

if u_i == 'z':
    animal = Zebra()
elif u_i == 'g':
    animal = Giraffe()
elif u_i == 'm':
    Moose()
elif u_i == 't':
    Tiger()

animal.growl()
