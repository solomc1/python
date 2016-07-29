from functools import reduce # for code_metric


# local function version  
# def separate(p,l):
#     def merge(f,r):
#         return (f[0]+r[0],f[1]+r[1])
#     if l == []:
#         return [],[]
#     else:
#         return merge( ([l[0]],[]) if p(l[0]) else ([],[l[0]]) , separate(p,l[1:]) )


# Assign once (and don't mutate version)
def separate(p,l):
    if l == []:
        return [],[]
    else:
        t_list,f_list = separate(p,l[1:])
        if p(l[0]):
            return [l[0]]+t_list, f_list
        else:
            return t_list       , [l[0]] + f_list


def is_sorted(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] < s[1] and is_sorted(s[1:])

# local function version  
# def sort(l):
#     def combine(low_high,mid):
#         return sort(low_high[0]) + [mid] + sort(low_high[1])
#     if l == []:
#         return []
#     else:
#         return combine (separate(lambda x : x<=l[0], l[1:]),l[0])
    
# Assign once (and don't mutate version)
def sort(l):
    if l == []:
        return []
    else:
        low,high = separate(lambda x : x<=l[0], l[1:])
        return sort(low) + [l[0]] + sort(high)

    
def compare(a,b):
    if a == '' and b =='':
        return '='
    elif a == '' and b !='':
        return '<'
    elif a != '' and b == '':
        return '>'
    
    if a[0] != b[0]:
        return '<' if a[0] < b[0] else '>'
    else:
        return compare(a[1:],b[1:])
    

def code_metric(file):
    #print([i for i in filter(lambda x : x.strip() != '',open(file))])
    #print([i for i in map(lambda x : (1,len(x.rstrip())),
    #             filter(lambda x : x.strip() != '',open(file)))])
    return reduce(lambda x,y : (x[0]+y[0],x[1]+y[1]),
               map(lambda x : (1,len(x.rstrip())),
                   filter(lambda x : x.strip() != '',open(file))))

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