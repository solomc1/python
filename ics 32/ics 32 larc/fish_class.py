class Goldfish:
    def feed(self):
        print("Feed Flakes")

class Shark:
    def feed(self):
        print("Feed Fish")

class Orca:
    def feed(self):
        print("Feed Humans")

u_i = input("Which fish do you want? ").lower()

if u_i == 'orca':
    fish = Orca()
elif u_i == 'shark':
    fish = Shark()
elif u_i == 'goldfish':
    fish = Goldfish()

##if type(fish) == Orca:
##    fish.humans()
##elif type(fish) == Goldfish:
##    fish.flakes()
##elif type(fish) == Shark:
##    fish.fish()
fish.feed()
