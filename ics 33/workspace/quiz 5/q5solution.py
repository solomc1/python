from functools import reduce # for code_metric


def separate(p,l):
    
    if l==[]:
        return ([],[])
    x = separate(p,l[1:])
    myTrue = x[0]
    myFalse = x[1]
    if p(l[0]):
        myTrue = [l[0]] + myTrue
    else:
        myFalse = [l[0]] + myFalse
    return (myTrue,myFalse)


def is_sorted(s):
    sort_s=sorted(s)
    if len(s) ==0:
        return True
    else:
        if s[0]!=sort_s[0]:
            return False
        else:
            s = s[1:]
            return is_sorted(s)
        
def sort(l): 
    pass
    if len(l) <= 1:
        return l
    result = []
    new_l = separate(lambda x: x<=l[0],l[1:]) 
    less_thans = sort(new_l[0])
    first_item = l[0]
    greater_thans = sort(new_l[1])
    result.extend(less_thans)
    result.append(first_item)
    result.extend(greater_thans) 
    return result 
    
def compare(a,b):
    if b == '' and a == '':
        return '='
    if a == '':
        return '<'
    elif b == '':
        return '>' 
    else:
        if a[0]<b[0]:
            return '<'
        elif a[0] >b[0]:
            return '>'
        else:
            a = a[1:]
            b = b[1:]
            return compare(a,b)
        if a[0] == b[0]:
            return '='
        

def code_metric(file):
    rfile = open(file).readlines()
    f = filter(lambda y: y.strip(),rfile)
    print(f)
    m = map(lambda x: (1,len(x.rstrip())), f)
    return reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]),m)






if __name__=="__main__":
    import predicate,random,driver
    from goody import irange
    
    driver.driver() # type quit in driver to return and execute code below
    
    print('Testing separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
     
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
    
    print('\nTesting sort')
    
    print('\nTesting compare')
    print(compare('','abc'))
    print(compare('abc',''))
    print(compare('',''))
    print(compare('abc','abc'))
    print(compare('bc','abc'))
    print(compare('abc','bc'))
    print(compare('aaaxc','aaabc'))
    print(compare('aaabc','aaaxc'))
    
    print('\nTesting code_metric')
    print(code_metric('cmtest.py'))
    print(code_metric('collatz.py'))
    print(code_metric('q5solution.py'))  # A function analyzing the file it is in
