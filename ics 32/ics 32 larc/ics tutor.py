def factorial (num: int) -> int:
    if num == 0:
        return 1
    return num* factorial (num-1)

factorial (5)

x=[5,6,[10,20[10,20]],10]

#recursion

def nested_sums(nums: list) -> int:
    result = 0
    for element in nums:
        if type(element) == int:
            result += element
        else:
            result +=nested(element)
    return result 
                
import os

print(os.path.exists("C://Users//blahblah")


#os.path.listdir(path) #returns list of file/directory name
#os.path.isfile(path) #returns true if path is file not directory
#os.path.getsize(path) finds size/amount of bytes
#os.path.isdir(path) returns true if path is a directory
#os.path.dirname(path) returns directory name

#Print out all the picture on my desktop that end in .jpg

def search_jpg(path: str) ->list:
    result = []
    for element in os.listdir(path):
        if element.endswith('.jpg'):
            result.append(element)
        elif os.path.isdir(element):
            result.extend(path + '\\' + search_jpg(element))
    return result
      

        









































