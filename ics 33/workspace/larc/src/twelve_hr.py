
import re
 
def to_24(input):
    # step 1
    pattern = "([1-9]|1[0-2]):([0-5]\d)([ap]m)"
    compiled = re.compile(pattern)
    matched = re.match(compiled, input)
    if matched == None:
        raise ValueError("Input time is in the wrong form! Cannot continue!")
     
    print(matched) # this should print out matched object
    print(matched.groups())
     
    hour, min, suffix = matched.groups()
    if suffix == "pm":
        if hour == "12":
            return hour + ":" + min
        return str(int(hour) + 12) + ":" + min
#         int(hour) --> int
#         int + 12 --> int + 12
#         str(int)
    elif suffix == "am":
        if hour == "12":
            return "00" + ":" + min
        return hour + ":" + min
         
         
print(to_24("4:30pm"))


        
        