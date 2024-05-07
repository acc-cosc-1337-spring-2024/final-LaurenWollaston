import random
class Stock():
    def __init__(self, symbol, name):
        self._symbol = symbol
        self._company_name = name
    def get_symbol(self):
        return(self._symbol)
    def get_company_name(self):
        return(self._company_name)
    
def addToDict(stock, dictionary):
    dictionary[stock.getSymbol()]=stock.getName()

def generateStock():
    stockNum = random.randint(0,4)
    if stockNum == 0:
        return(Stock('AAPL','Apple Inc'))
    elif stockNum == 1:
        return(Stock('CAT','Caterpillar'))
    elif stockNum == 2:
        return(Stock('EK','Eastman Kodak'))
    elif stockNum == 3:
        return(Stock('GOOG','Google'))
    elif stockNum == 5:
        return(Stock('MSFT','Microsoft'))
    else:
        print('Unexpected error, this shouldn\'t appear. ¯\_(ツ)_/¯' )