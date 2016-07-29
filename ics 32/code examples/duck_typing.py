# duck_typing.py
#
# ICS 32 Winter 2014
# Code Example
#
# This module makes use of Python's "duck typing" feature by implementing
# five classes that all have the same interface, meaning that objects of
# these classes can be used interchangeably.  Each class represents some
# kind of operation that can be performed on a single input; asking an
# object of one of these classes to "calculate" is how you ask it to
# perform its operation.
#
# Collectively, we'll say that objects of these classes are "calculations"
# (i.e., you can ask them to calculate something, by giving them a value
# and expecting some value back).  In general, a "calculation" (in our
# definition here) is an object that has a method "calculate" that
# takes a single parameter (in addition to "self").

import math



class SquareCalculation:
    def calculate(self, n):
        return n * n


class LengthCalculation:
    def calculate(self, n):
        return len(n)


class SquareRootCalculation:
    def calculate(self, n: float) -> float:
        return math.sqrt(n)


class MultiplyByCalculation:
    def __init__(self, multiplier: float):
        self._multiplier = multiplier

    def calculate(self, n: float) -> float:
        return n * self._multiplier


class CubeCalculation:
    def calculate(self, n: float) -> float:
        return n * n * n



# As an example of a function that uses these classes, consider this
# one called run_calculations, which takes a list of calculations and
# a starting value, and applies the calculations in sequence (i.e.,
# the first calculation is run against the starting value, the second
# is run against the result of the first, the third is run against the
# result of the second, and so on).  The result of the last calculation
# in the list is the overall result.

def run_calculations(calculations: 'list of calculations', starting_value):
    current_value = starting_value

    for calculation in calculations:
        current_value = calculation.calculate(current_value)

    return current_value
    

# The thing to notice about run_calculations is that it doesn't have any
# code in it that checks types.  There's nothing like this:
#
#     if type(x) == Square:
#         square the number
#     elif type(x) == MultiplyBy:
#         multiply the number
#     ...
#
# Why that's such a good thing is because we can add new kinds of
# calculations by simply writing new classes that implement the
# same interface (i.e., that have the appropriate calculate method),
# without ever having to touch run_calculations again, yet
# run_calculations will work automatically with the new kinds of
# objects.  One of the goals when we write ever-larger programs is
# isolating the effect of changes, so anything we can do to prevent
# one change from causing cascading changes in many other places is
# a big win.
#
# Try executing this module and then evaluating these expressions in
# the Python interpreter.  Before you evaluate each one, decide what
# you think its outcome should be.
#
#     run_calculations([SquareCalculation(), SquareCalculation()], 4)
#     run_calculations([LengthCalculation(), MultiplyByCalculation(2)], 'Boo')
#     run_calculations([], 80)
#
# Now try writing a new class that implements the operation of your
# choice.  Re-execute this module (after writing your new class) and
# try calling run_calculations and passing it an object of your class.
# Voila!  Works fine!
#
# I should note here that this appears to be similar to the idea of
# passing functions as parameters to other functions, and, indeed, it
# is.  Where it differs, though, is that the objects we're creating
# are capable of carrying state with them, whereas functions are 
# limited to accessing the parameters that are passed to them.
# So, for example, our MultiplyBy class takes a parameter to its
# constructor; its __init__ method stores it in an attribute, and that
# attribute is then available at the time the calculate() method is
# called.  This is not actually as mind-bending as it sounds; since
# calculate() is a method, it accepts an additional "self" parameter,
# and the attribute "_multiplier" actually belongs to the "self"
# object.
