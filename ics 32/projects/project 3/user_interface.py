#Solomon Chan 40786337

import datetime
import download_quotes
import indicators
import signal_strategies

def get_start_date()->datetime.date:
    '''asks the user to enter start date'''
    date_str = input("Enter start day of analysis(format- YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        if date > datetime.date.today():
            print('Start date cannot be in the future. Please try again.')
            return get_start_date()

        elif date == datetime.date.today():
            print('Start date cannot be today. When would the end date be? Please try again.')
            return get_start_date()

        else:
            return date
    except:
        print('Incorrect format. Please try again.')
        return get_start_date()

def get_end_date(start_date)->datetime.date:
    '''asks the user to enter end date'''
    date_str = input("Enter end day of analysis(format- YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

        if date > datetime.date.today():
            print('End date cannot be in the future. Please try again.')
            return get_end_date(start_date)

        elif start_date >= date:
            print('The end date must be in the future of the start date. Please try again.')

        else:
            return date
    except:
        print('Incorrect format. Please try again.')
        return get_end_date(start_date)

        
def get_strategy()->list:
    strategy = input("Choose(S)imple moving average or (D)irectional indicator: ").upper()
    if strategy == "S" or strategy == "D":
        return strategy
    else:
        print("Invalid input, try again")
        return get_strategy()
    
        
        

def get_number():
    try:
        number = (int(input("Enter the number of days: ")))
    except:
        print("Invalid input, please try again")
        return get_number()
    else:
        if number >0:
            return number
        else:
            print("number must be greater than 0")
            return get_number()

def yahoo(symbol,start_year,start_month, start_day,end_year,end_month,end_day):
    return download_quotes.print_closing_price_list(symbol,start_year,start_month, start_day,end_year,end_month,end_day )
    

def string_to_float(lst:list)->list:
    result = []
    for i in lst:
        result.append(float(i))
    return result


        

        
def format_s(dates:list, closing_price_list:list, indicator_list:list, signal_list:list)->str:
    for i in range(len(dates)):
        print('{}   {}   {}      {}'.format(dates[i], closing_price_list[i],indicator_list[i], signal_list[i]))

def format_d(dates:list, closing_price_list:list, indicator_list:list, signal_list:list)->str:
    for i in range(len(dates)):
        print('{}   {}     {:+}   {:>12}'.format(dates[i], closing_price_list[i],indicator_list[i], signal_list[i]))

        
def buy_num()->int:
    try:
        buy_numbs = int(input("Buy Threshold: "))
    except:
        print("Invalid format, Please try again")
        return buy_num()
    else:
        return buy_numbs
    
def sell_num()->int:
    try:
        sell_numbs = int(input("Sell Threshold (negative sign added already no need to type: "))
    except:
        print("Invalid format, Please try again")
        return sell_num()
    else:
        return sell_numbs

    
    
def user_interface():
    try:
        print("Welcome to the place to earn money!")
        symbol = input("Enter the company ticker symbol: ").upper()

        start_date = get_start_date()
        end_date = get_end_date(start_date)
        
        start_year = start_date.year
        start_month = start_date.month - 1
        start_day = start_date.day
        end_year = end_date.year
        end_month = end_date.month - 1
        end_day = end_date.day

        strategy = get_strategy()
        num = get_number()
        dates = download_quotes.print_dates(symbol,start_year,start_month, start_day,end_year,end_month,end_day) 
        closing_price_list =  download_quotes.print_closing_price_list(symbol,start_year,start_month, start_day,end_year,end_month,end_day)
        closing_price_list = string_to_float(closing_price_list)
        
    except:
        print("Unknown Error, restarting...")
        user_interface()
    else:
        
    
        if strategy == 'S':
            indicator_list = indicators.simple_moving_average.execute(closing_price_list,num)
            signal_list = signal_strategies.simple_moving_average_signal.signals(closing_price_list,indicator_list)
            print()
            print("SYMBOL: " + symbol)
            print("SRATEGY: Simple moving average (" + str(num) + "-day)")
            print()
            print("DATE         CLOSE   INDICATOR  SIGNAL")   
            format_s(dates, closing_price_list, indicator_list, signal_list)
            
                           
         
        elif strategy == 'D':
            indicator_list = indicators.directional_indicator.execute(closing_price_list,num)
            buy_number =buy_num()
            sell_number = sell_num()
            signal_list = signal_strategies.directional_signal.direction(closing_price_list,indicator_list,buy_number,sell_number)
            print()
            print("SYMBOL: " + symbol)
            print("SRATEGY: Directional (" + str(num) + "-day), Buy above: +"+ str(buy_number)+ ",  Sell below: -" + str(sell_number))
            print()
            print("DATE         CLOSE   INDICATOR     SIGNAL")   
            format_d(dates, closing_price_list, indicator_list, signal_list)
        
        print("Goodbye!")
       
if __name__ == '__main__':
    user_interface()
