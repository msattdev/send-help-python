def getChessSquareColor(column, row):
    if column < 0 or column > 7 or row < 0 or row > 7:
        return ''  
    elif (column % 2 == 0 and row % 2 == 0) or (column % 2 == 1 and row % 2 == 1):
        return 'white'
    elif (column % 2 == 1 and row % 2 == 0) or (column % 2 == 0 and row % 2 == 1):
        return 'black'
    

assert getChessSquareColor(0, 0) == 'white'
assert getChessSquareColor(1, 0) == 'black'
assert getChessSquareColor(0, 1) == 'black'
assert getChessSquareColor(7, 7) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''