def create_multiplication_table():
    mTable = [[1,2,3,4,5,6,7,8,9,10]]
    for i in range(2,6):
        newRow = [i*row1Val for row1Val in mTable[0]]
        mTable.append(newRow)
    return mTable

def display_multiplication_table(table):
    for i in range(0,(len(table))):
        print(table[i])
