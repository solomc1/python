class adder:
    def __init__(self, x: int) -> None:
        self._x = x

    def sum(self, y: int) -> int:
        return self._x + y

a = adder(5)
print(a.sum(10))

b = adder(10)
print(b.sum(9))
adder.sum(a, 10)


class mather:
    def __init__(self, x: int) -> None:
        self._x = x

    def sum(self, y: int) -> int:
        return self._x + y

    def diff(self, y: int) -> int:
        return self._x - y

    def mult(self, y: int) -> int:
        return self._x * y

    def quot(self, y: int) -> float:
        return self._x / y

a = mather(5)
print(a.sum(4))

b = mather(8)
print(b.diff(4))

c = mather(3)
print(c.mult(4))

d = mather(9)
print(d.quot(2))





class subtractr:
    def __init__(self, x: int) -> None:
        self._x = x

    def sub(self, y:int) -> None:
        self._x -= y

    def get(self) -> int:
        return self._x

x = subtractr(100)
x.sub(5)
print(x.get())



#Create your own class to do whatever you want it


class exponential:
    def __init__ (self, x: int) -> None:
        self._x = x

    def power(self, y:int) -> None:
        self._x **=y

    def get(self) -> int:
        return self._x


a = exponential(3)
a.power(2)
print(a.get())


class factorial:
    def __init__ (self, x: int) -> None:
        self._x = x

    def factor(self, y:int) -> None:
        if y == 0:
            return 1
        return y * self.factor(y-1)

    def get(self) -> int:
        return self._x

a = factorial(5)
a.factor(3)
print(a.get())
    


