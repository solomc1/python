#### WHAT I WANT 

# >>> c = Counter()
# >>> c.count()
#1
#>>> c.count()
#2
# >>> c.current()               Counter.current(c)
#2
# >>> c.current()
# 2
# >>>> c.reset()
# >>>> c.current()
# 0
# >>> c.count()
# 1
# >>> c.count()
# 1
# c2= Counter()
# >>> c2.current()
# 0


class Counter:
    def __init__(self):
        self._count = 0

    def current(self)-> int:
        return self._count

    def count(self) -> int:
        self._count += 1
        return self._count

    def reset(self)-> None:
        self._count = 0





        



















        

    
