class indicator_simple:
    def __init__(self, days: int):
        self._days = days

    def indicate(self, prices: list) -> list:
        result = [ ]
        for i in range(len(prices)):
            if i + 1 < self._days:
                result.append('')
            else:
                start = i - (self._days - 1)
                end = i + 1
                total = sum(prices[start:end])
                result.append('{:.2f}'.format(total/self._days))
        return result

class signal_simple:
    def __init__(self, prices: list):
        self._prices = prices

    def signal(self, indicators: list) -> list:
        sell = False
        buy = False
        result = [ ]
        for i in range(len(indicators)):
            if indicators[i] == '' or indicators[i-1] == '':
                result.append('')
            else:
                if self._prices[i] > float(indicators[i]):
                    if buy == False:
                        result.append('BUY')
                        buy = True
                        sell = False
                    else:
                        result.append('')
                elif self._prices[i] < float(indicators[i]):
                    if sell == False:
                        result.append('SELL')
                        sell = True
                        buy = False
                    else:
                        result.append('')
                else:
                    result.append('')
                    sell = False
                    buy = False
        return result
                


##import download
##from stocks import *
##url = 'http://ichart.yahoo.com/table.csv?s=A&a=2&b=1&c=2012&d=10&e=30&f=2012&g=d'
##info = download.download(url)
##prices = info_to_prices(info)
##dates = info_to_dates(info)
##indic = indicator_simple(3)
##ilist = indic.indicate(prices)
##s = signal_simple(prices)
##slist = s.signal(ilist)
##x = []
##for i in prices:
##    x.append(i)
##    
##stock_format(x, prices, ilist, slist)
##
