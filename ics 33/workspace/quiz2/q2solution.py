import re

# Use day_dict and is_leap_year in your tomorrow function

day_dict ={ 1 : 31,
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
           10 : 31, 
           11 : 30,
           12 : 31} 

def is_leap_year(month:int)->bool:
    return (month%4 == 0 and month%100 != 0) or month%400==0

def days_in(month:int,year:int)->int:
    return (29 if month==2 and is_leap_year(year) else day_dict[month])


def tomorrow(date:str)->str:
    pattern = "^([1-9]|1[012])/(0?[1-9]|[1-2]\d|3[01])/(\d{2}|\d{4})$"
    compiled = re.compile(pattern)
    matched = re.match(compiled, date)
    if matched == None:
        raise AssertionError("Input date invalid!")
    month, day, year = matched.groups()
    month = int(month);day = int(day)
    year = int(year)
    if len(matched.group(3))==2:
        year+=2000
    if day> days_in(month, year):
        raise AssertionError("Input date invalid!")
    day+=1
    if day> days_in(month, year):
        month+=1;day =1
    if month>12:
        month = 1;year+=1    
    return ("{}/{}/{}".format(month,day,year))
    

if __name__ == '__main__':
    import driver, prompt,traceback
    while True:
        date = prompt.for_string('Enter date to test (quit to start driver)')
        if date == 'quit':
            break;
        try:
            print('tomorrow=',tomorrow(date))
        except:
            print('tomorrow raised exception')
            traceback.print_exc()
        
    driver.driver()
