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

def is_leap_year(year:int)->bool:
    return (year%4 == 0 and year%100 != 0) or year%400==0

def days_in(month:int,year:int)->int:
    return (29 if month==2 and is_leap_year(year) else day_dict[month])


def tomorrow(date:str)->str:
    m = re.match(r'([1-9]|1[0-2])/(0?[1-9]|[1-2]\d|3[01])/((?:\d\d)?\d\d)$',date)
    assert m, 'q2solution.tomorrow: date format('+str(date)+') incorrect'
    month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    year += (0 if len(m.group(3))==4 else 2000)
    assert 1<=day<=days_in(month,year), 'tomorrow: day('+str(day)+') in date('+str(date)+') incorrect'
    day += 1
    if day > days_in(month,year):
        day,month = 1,month+1
    if month > 12:
        month,year = 1, year+1
    return str(month)+'/'+str(day)+'/'+(4-len(str(year)))*'0'+str(year)



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
