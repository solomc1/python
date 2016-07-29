def count_num(s,l):
    result = {}
    for key in s:
        val = l.count(key)
        if val>0:
            result[key]=val
    return result

a = set(['a','b'])
b = ['a', 'a', 'a', 'z', 'c', 'b']

count_num(a,b) 