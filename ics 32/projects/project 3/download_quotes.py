#Solomon Chan 40786337


import urllib.request
import user_interface


def print_dates(symbol:str,start_year:int, start_month:int,start_day:int, end_year:int, end_month:int,end_day:int) -> None:
    
    url = _yahoo_url(symbol,start_year,start_month,start_day,end_year,end_month,end_day)
    return _get_dates(url)

def print_closing_price_list(symbol:str,start_year:int, start_month:int,start_day:int, end_year:int, end_month:int,end_day:int) -> None:
    
    url = _yahoo_url(symbol,start_year,start_month,start_day,end_year,end_month,end_day)
    return _get_closing_price(url)


def _yahoo_url(symbol:str,start_year:int, start_month:int,start_day:int, end_year:int, end_month:int,end_day:int)->str:
    
    return ('http://ichart.yahoo.com/table.csv?s='+ symbol+'&a=' +str(start_month)+ '&b='+ str(start_day) +'&c='+str(start_year) +'&d='+str(end_month)+'&e='+str(end_day) +'&f=' + str(end_year) +'&g=d').strip()



def _get_dates(url: str) -> None:
    result = []
    try:
        response = urllib.request.urlopen(url)

    except:
        print("failed to download url")
        user_interface.user_interface()

    else:
        content_bytes = response.read()
        content_string = content_bytes.decode(encoding='utf-8')
        content_lines = content_string.splitlines()
        for element in content_lines[1:]:
            content_lst = element.split(',')
            result.append(content_lst[0])
        return result        
            


def _get_closing_price(url: str) -> None:
    result = []
    try:
        response = urllib.request.urlopen(url)

    except:
        print("failed to download url")
        user_interface.user_interface()

    else:
        content_bytes = response.read()
        content_string = content_bytes.decode(encoding='utf-8')
        content_lines = content_string.splitlines()
        for element in content_lines[1:]:
            content_lst = element.split(',')
            result.append(content_lst[-1])
        return result




        





        



