##def print_strings(lst: [str]) -> list:
##    result = []
##    for element in lst:
##        if type(element) == str:
##            result.append(element)
##        else:
##            result.extend(return_strings(element))
##    return result
##
##print(return_string(['a','b',['c',['d']],'e']))
##
##def divider() -> None:
##    while True:
##        try:
##            n = int(n)
##            print (n/5)
##        except:
##           print('Your "number" was invalid.')
##
##divider()
##
##
##
##
##
##def adder()-> None:
##    while True: 
##        try:
##            x = int(input("Please enter the number you would like to add by 2:  a"))
##            print (x+2)
##            break
##        
##        except:
##            print("error")
##    return
##
##adder()
##                  
            
        
#os.path.exists(path: str)

# Create a program to print out all the files in a path specified by the user.
#Your program should not crash, given bad input.

#os.path.join(p1,p2) =

import os

def print_files(path: str) ->[str]:
    result = []
    for element in os.listdir(path):
        new_path = os.path.join(path,element)
        if os.path.isfile(path):
            result.append(element)
        else:
            result.extend(print_files)
    return result
        
        
    
#os.path.isfile(path: str)

def path_exists() -> None:
    n = input("Enter a path: ")
    if os.path.exists(n):
        print_files(path)
    else:
        print("error")
    
#os.path.exists









































