#Solomon Chan 40786337

import indicators

class simple_moving_average_signal:
        
    def signals(values:list, indicator_list:list)->list:
        result = []
        buy = False
        sell = False
        key=0
        if is_nothing(indicator_list):
            for i in range(len(indicator_list)):
                result.append('')
        else:
            indicator_list = str_to_zero(indicator_list)
            for i in range(len(indicator_list)):
                if indicator_list[i-1] == '' or indicator_list[i] == '':
                    result.append('')
                    key=i
                else:
                    if float(indicator_list[i]) < float(values[i]):
                        if buy == False:
                            result.append('BUY')
                            buy = True
                            sell = False
                           
                        else:
                            result.append('')
                    elif float(indicator_list[i])> float(values[i]):
                        if sell == False:
                            result.append('SELL')
                            buy = False
                            sell = True
                            

                        else:
                            result.append('')
                    else:
                        result.append('')
                        buy = False
                        sell = False
                        
            if float(indicator_list[key])<float(values[key]) and float(indicator_list[key+1])>float(values[key+1]):
                result[key+1] = 'BUY'
            elif float(indicator_list[key])>float(values[key]) and float(indicator_list[key+1])<float(values[key+1]):
                result[key+1] = 'SELL'
            else:
                result[key+1] = ''
        return result


class directional_signal:
        
    def direction(values:list, directional_list:list,buy_num:int,sell_num:int)->list:
        result = []
        for i in range(len(values)):
            if i ==0:
                result.append('')
                
            else:
                if directional_list[i] > buy_num:
                    if directional_list[i-1]<= buy_num:
                        result.append('BUY')
                    else:
                        result.append('')
                        
                                
                elif directional_list[i]< sell_num:
                    if directional_list[i-1]>= sell_num:
                        result.append('SELL')
                    else:
                        result.append('')
                                        
                else:
                    result.append('')
                                   
        return result

    
def is_nothing(lst:list)-> bool:
    for i in lst:
        if i != '':
            return False
        else:
            return True
    
def str_to_zero(lst:list)->list:
    result = []
    for i in lst:
        if i == '':
            result.append(0)
        else:
            result.append(i)
    return result

