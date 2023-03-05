# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from sudoku import Sudoku

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    startingSudoku =[
        [0, 0, 0, 8, 1, 0, 0, 4, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 6],
        [3, 4, 0, 7, 2, 0, 9, 0, 0],
        [0, 0, 0, 4, 3, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [5, 0, 0, 1, 0, 0, 4, 7, 0],
        [0, 0, 0, 0, 0, 9, 0, 5, 0],
        [0, 0, 0, 0, 0, 9, 0, 5, 0]
        ]
    printTest = []
    printIndex = []
    range(9)
    for inx, x in enumerate(startingSudoku):
        printTest.append(x[3])
        printIndex.append(inx)
    print(printTest)
    print(printIndex)

    sudoku = Sudoku(startingSudoku)

    for ind, numset in enumerate(sudoku.getSets()):
        for num in numset.getNumbers():
            print(str(type(numset)) + " " + str(ind) + " set; x = " + str(num.getX()) + " y = " + str(num.getY()))


