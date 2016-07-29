#### 1. More try and excepts
##try:
##    try:
##        a = [1,2,3]
##        b = 4
##        c = 2 #c = 5
##        print(a[b])
##    except:
##        d = 3
##        print(a[d])
##    else:
##        e = 1
##        print(a[e])
##    finally:
##        print(a[c])
##except:
##    print('failure')
##else:
##    print('success')
##finally:
##    print('done')
###3
###failure
###done
##    
##
#### **What happens if c = 5?**
##
###failure
###done
    
## 2. More module importing
"1.py"
import 1
print("1")
if __name__ == '__main__':
    print('1.1')

    #1
    #1
    #1.1

"2.py"
if __name__ == '__main__':
    import 1
    import 2
    import 3
    import 4
    print('2.2')

    #1
    #four
    #2.2

"3.py"
import 1
import 2
import 3
import 4
if __name__ == '__main__':
    print('3.3')
    #1
    #four
    #3.3

"4.py"
print(__name__)

    #__name__


 More recursive practice
 write a function that takes a nested list of characters and returns
  one string concatenating all of them.
 ex: input = ['l', ['a', 'r'], 'c', ['i', 'c', 's', ['3']], '2']
     output = larcics32

def string_concat(l: list) -> str:
    
    if len(l) == 0:
        return None
    result = ''
    
    for element in l:
        if type(element)== list:
            result += string_concat(element)
        else:
            result += element
    return result

##print(string_concat(['l', ['a', 'r'], 'c', ['i', 'c', 's', ['3']], '2']))
##
###append elements
#extend lists
#+= str 


## learn definitions!
## -sockets--  In Python, sockets are objects that encapsulate
## and hide many of the underlying details of how a program can connect
## directly to another program
## -protocol-- which is a set of rules governing what each party will send
##  and receive, and when they will do it.
## -module  A module can define functions, classes and variables.
##  A module can also include runnable code.
## -method-- methods aren't quite like functions; they get called on an object
## -anything else that he spent more than 10 minutes on in class
## http://domain:port/resources -> http://www.ics.uci.edu:80/~thornton












