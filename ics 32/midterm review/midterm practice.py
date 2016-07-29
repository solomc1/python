## If you want to run the code, you should comment out the problems you haven't
##  done yet so you can't see the answers for them.
## Hints for each problem are at the bottom of this file
##
## 1. What's the output of the following code? 
##try:
##    try:
##        a = 5
##        b = 7
##        c = "five"
##        d = "seven"
##        print(a*c)
##        print(c+d)
##    except:
##        print(b*c)
##    else:
##        print(c*d)
##    finally:
##        print("first finally")
##except:
##    print("second except")
##else:
##    print("second else")
##finally:
##    print("second finally")
##
##Answers
##fivefivefivefivefive
##fiveseven
##first finally
##second except
##second finally
##
##
### 2. Imagine you have 3 modules as seen below
##"first.py"
##import second
##print("1")
##if __name__ == '__main__':
##    print("first main")
##
##"second.py"
##import third
##print("2")
##if __name__ == '__main__':
##    import first
##    print("second main")
##
##"third.py"
##print("3")
##if __name__ == '__main__':
##    import second
##    print("third main")
##
### What is the output if
##  a) first.py is run,
##      3
##      2
##      1
##      first main
##       
##       
##  b) second.py is run, and
##       3
##       2
##       2
##       1
##       second main
##       
##       
##       
##
##
##  c) third.py is run?
##       3
##       3
##       2
##       third main
##
##
## 3. What's wrong with the following class? Just try to fix the class,
##  don't fix anything in the if name = main block
##class Person:
##    def __init__(name):  
##        self.name = name 
##    def grow_up():      
##        self.age += self.age + 1 
##                                 
##    if __name__ == '__main__':
##        a = Person("Alex")
##        a.grow_up() #Person.grow_up(a)
##
###Answers
##
##    
##
##class Person:
##    def __init__(self, name: str):
##        self._name = name
##        self._age = 0
##    def grow_up(self)->int:
##        self._age += 1
##        
##
##
##if __name__ == '__main__':
##    a = Person("Alex")
##    a.grow_up()
##
##
## 
##
##
## 4. Write a function that takes a nested list of integers and returns the
##  minimum. Below is a function definition but you need to fill in the body.
## Remember that a nested list of integers means that every element in the list
## is either an int or a nested list of ints.
##def find_min(l: list) -> int:
##    if len(l) == 0:
##        return 0            
##    result = []
##    for element in l:
##        if type(element) == list:
##            find_min(element)
##        else:
##            result.append(element)
##        result.sort()
##    return result
##        #return min(result)
##l = [[100,200,40],33,22,100,99,[33,76,54],1,33,20,21]
##print(find_min(l))
##
##def recursive_min2 (l: 'nested list of ints')-> int:
##    if len(l) == 0:
##        return None
##    minimum = l[0]
##    for item in l:
##        if type(item) == int:
##            if item <minimum:
##                minimum = item
##            elif recursive_min2(item) <minimum:
##                minimum = recursive_min2(item)
##    return minimum
##
##
##def rmin(l:list) -> int:
##    if len(l) == 0:
##        return N
##    minim = l[0]
##    for element in l:
##        if type(minim) == list:
##            minim = rmin(minim)
##        if type(element) == int:
##            if type(element) < minim:
##                minim = element
##        elif rmin(element) < minim:
##            minim = rmin(element)
##    return minim
##                    
##
## 5. What does the underscore before a function mean?
##
##private function should not be called outside of a module, a helper function,
##used by other functions in the module shouldn't access outside the module
##
##
##
##
##
## 6. What does the if __name__ == '__main__' statement mean?
## if the code is imported, then the functions will be stored, but will not run.
##However, if the code is ran by itself, the code will run.
##only execute the code if the module is the original main module.
##if its imported, it will not run.
##
##
##
##
##
##
## Read all his code examples for review. If you understand everything he
##  wrote in his code examples, as well as what you did in projects,
##  you should be fine.
## Things to look over that I didn't go in depth about:
##  the sockets, protocol, and classes code examples.
## Make sure you're able to write your own classes!
## On Wednesday I'll be going over any questions you might have, so make sure
##  to bring them!
## protocol- set of rules governing what each party will send and receive,
## and when then will do it. protocol is like a rigidly defined kind of
## of conversation with each participating knowing its role, so it knows what
## to say at any given time
##
##
##
##
##
##
##
##
## Hints 
## 1. Remember what each word means. When do you do the except and else
##  blocks? When in doubt, always do finally!
##
## 2. If a module is loaded once through import, it doesn't load again, even if
##  the same import is called again. Python is smart enough to remember what
##  modules have been loaded already
##
## 3. Remember what we went over in class about classes. What always has to be
##  inside a class? There's 2 problems only, but they might be found in multiple
##  places
##
## 4. With recursion, always start small. How do you find the minimum of a simple
##  list of integers? After you get that, seperate it into the differnt possible
##  cases and deal with each seperately.
##
##
##
##
##
##
##
##
##
##
##
##
##
##        
##
