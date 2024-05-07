class Stock():
    def __init__(self, symbol, name):
        self._symbol = symbol
        self._company_name = name
    def getSymbol(self):
        return(self._symbol)
    def getName(self):
        return(self._company_name)
    
def addToDict(stock, dictionary):
    dictionary[stock.getSymbol()]=stock.getName()
    
def stock_purchace_history():
    purchaceRecord = {}
    apple = Stock('AAPL','Apple Inc')
    cater = Stock('CAT','Caterpillar')
    kodak = Stock('EK','Eastman Kodak')
    google = Stock('GOOG','Google')
    MS = Stock('MSFT','Microsoft')
    addToDict(apple, purchaceRecord)
    addToDict(cater, purchaceRecord)
    addToDict(kodak, purchaceRecord)
    addToDict(google, purchaceRecord)
    addToDict(MS,purchaceRecord)
    for key, val in purchaceRecord.items():
        print(key, val)