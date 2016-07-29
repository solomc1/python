## 1. More try and excepts
##try:
##    try:
##        a = [1,2,3]
##        b = 4
##        c = 2
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

##3
##failure
##done
    
## **What happens if c = 5?**
##failure
##done


##
## 2. More module importing
##"1.py"
##import 1
##print("1")
##if __name__ == '__main__':
##    print('1.1')
##    #1
##    #1
##    #1.1
##
##"2.py"
##if __name__ == '__main__':
##    import 1
##    import 2
##    import 3
##    import 4
##    print('2.2')
##    #1
##    #fourth
##    #2.2
##
##"3.py"
##import 1
##import 2
##import 3
##import 4
##
##if __name__ == '__main__':
##    print('3.3')
##    #1
##    #fourth
##    #3.3
##
##"4.py"
##print(__name__)
###__main__


## More recursive practice
#### write a function that takes a nested list of characters and returns
####  one string concatenating all of them.
#### ex: input = ['l', ['a', 'r'], 'c', ['i', 'c', 's', ['3']], '2']
####     output = larcics32
##
##def string_concat(l: list) -> str:
##    if len(l) == 0:
##        return None
##    result = ''
##    
##    for element in l:
##        if type(element)== list:
##            result += string_concat(element)
##        else:
##            result += element
##    return result
##
##print(string_concat(['l', ['a', 'r'], 'c', ['i', 'c', 's', ['3']], '2']))
##            
##
##
#### learn definitions!
## -sockets
## -protocol
## -module
## -anything else that he spent more than 10 minutes on in class












