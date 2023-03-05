import numpy as np


class Sudoku:

    def __init__(self, matrix):
        self.__numberOfSets = 27
        self.Numbers = []
        self.Sets = []
        self.generateNumbers(matrix)
        self.generateSets()

    def generateNumbers(self, matrix):
        for inx, x in enumerate(matrix):
            for iny, y in enumerate(x):
                self.Numbers.append(Number(y, inx, iny))

    def generateSets(self):
        # add horizontal sets to list
        for number in self.Numbers:
            if number.getX() == 0:
                self.Sets.append(HorizontalSet(self.Numbers, number))
        # add vertical sets to list
        for number in self.Numbers:
            if number.getY() == 0:
                self.Sets.append(VerticalSet(self.Numbers, number))
        # add square sets to list
        for number in self.Numbers:
            if number.getX() == 0 or number.getX() == 3 or number.getX() == 6:
                if number.getY() == 0 or number.getY() == 3 or number.getY() == 6:
                    self.Sets.append(SquareSet(self.Numbers, number))

    def setNumberSetLists(self):
        for number in self.Numbers:
            number.setSets(self.Sets)

    def getNumbers(self):
        return self.Numbers
    def getSets(self):
        return self.Sets


class Number:
    def __init__(self, value, xLocation, yLocation):
        self.__location = [xLocation, yLocation]
        self.Sets = []
        if value == 0:
            self.__value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.__value = value

    def setSets(self, sets):
        for set in sets:
            if self.numberInSet(set):
                self.Sets.append(set)

    def numberInSet(self, set):
        numberIsInSet = False
        for number in set:
            if self == number:
                numberIsInSet = True
                break
        return numberIsInSet

    def getX(self):
        return self.__location[0]

    def getY(self):
        return self.__location[1]


class Set:
    def __init__(self, numbers, number):
        self.__numberOfNumbers = 9
        self.Numbers = []
        self.setNumbers(numbers, number)

    def setNumbers(self, numbers, number):
        pass

    def getNumbers(self):
        return self.Numbers


class SquareSet(Set):
    def __init__(self, numbers, number):
        super().__init__(numbers, number)

    def setNumbers(self, numbers, number):
        print("number passed to create square set" + str(number.getX()) + str(number.getY()))
        for num in numbers:
            if num.getX() == number.getX() or num.getX() == number.getX() + 1 or num.getX() == number.getX() + 2:
                print("first if gate " + str(num.getX()) + str(num.getY()))
                if num.getY() == number.getY() or num.getY() == number.getY() + 1 or num.getY() == number.getY() + 2:
                    print("second if gate " + str(num.getX()) + str(num.getY()))
                    self.Numbers.append(num)


class HorizontalSet(Set):
    def __init__(self, numbers, number):
        super().__init__(numbers, number)

    def setNumbers(self, numbers, number):
        for num in numbers:
            if num.getY() == number.getY():
                self.Numbers.append(num)


class VerticalSet(Set):
    def __init__(self, numbers, number):
        super().__init__(numbers, number)

    def setNumbers(self, numbers, number):
        for num in numbers:
            if num.getX() == number.getX():
                self.Numbers.append(num)
