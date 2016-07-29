#Solomon Chan 40786337

class simple_moving_average:

    def execute(closing_price_list:list, number_of_days:int)->list:
        result = []
        
        for n in range(len(closing_price_list)):
            if n + 1 < number_of_days:
                result.append('')
            else:                  
                initial= n- (number_of_days-1)
                final = n +1
                s = sum(closing_price_list[initial:final])
                result.append('{:.2f}'.format(s/number_of_days))
  
        return result

class directional_indicator:
    def execute(closing_price_list:list,number_of_days:int)->list:
        result = []
        for n in range(len(closing_price_list)):
            
            increase = 0
            decrease = 0
            if n != 0:
                if n < number_of_days-1:
                    initial = 1
                    final = n+1
                else:
                    initial = n - (number_of_days-1)
                    
                    final = n + 1
                
                for i in range(initial,final):
                    if closing_price_list[i-1] < closing_price_list[i]:
                        increase += 1
                        
                    elif closing_price_list[i-1] > closing_price_list[i]:
                        decrease += 1
                        
                
            indicator = increase - decrease
            result.append(indicator)
        return result

