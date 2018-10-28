import unittest
import algo
import random


class TestAlgo(unittest.TestCase):

    def setUp(self):
        self.seat = [[1, 2, 3, 4, 5, 6, 7],
                     [8, 9, 10, 11, 12, 13, 14],
                     [15, 16, 17, 18, 19, 20, 21],
                     [22, 23, 24, 25, 26, 27, 28],
                     [29, 30, 31, 32, 33, 34, 35],
                     [0, 0, 36, 37, 38, 0, 0]]
        self.ran = random.Random()

    # to test if it can generate correct form of seat
    def testGen(self):
        seat = algo.generateSeats()

        def check(arr):
            num_list = []
            if len(arr) != 6 or len(arr[0]) != 7:
                return False
            if arr[5][0] != 0 or arr[5][1] != 0 or arr[5][5] != 0 or arr[5][5] != 0 or arr[5][6] != 0:
                return False
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if arr[i][j] != 0:
                        num_list.append(arr[i][j])
            num_list = set(num_list)
            return len(num_list) == 38
        self.assertTrue(check(seat))

    # to test shift left on row 1
    def testShiftLeftRow1(self):
        col = self.ran.randint(2, 7)
        new = algo.shiftLeft(1, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(1, 6):
                if new[i] != old[i]:
                    return False
            return new[0] == [2, 3, 4, 5, 6, 7, 1]
        self.assertTrue(check(self.seat, new))

    # to test shift left on row 2
    def testShiftLeftRow2(self):
        col = self.ran.randint(2, 7)
        new = algo.shiftLeft(2, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 1:
                    if new[i] != old[i]:
                        return False
            return new[1] == [9, 10, 11, 12, 13, 14, 8]
        self.assertTrue(check(self.seat, new))

    # to test shift left on row 3
    def testShiftLeftRow3(self):
        col = self.ran.randint(2, 7)
        new = algo.shiftLeft(3, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 2:
                    if new[i] != old[i]:
                        return False
            return new[2] == [16, 17, 18, 19, 20, 21, 15]
        self.assertTrue(check(self.seat, new))

    # to test shift left on row 4
    def testShiftLeftRow4(self):
        col = self.ran.randint(2, 7)
        new = algo.shiftLeft(4, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 3:
                    if new[i] != old[i]:
                        return False
            return new[3] == [23, 24, 25, 26, 27, 28, 22]
        self.assertTrue(check(self.seat, new))

    # to test shift left on row 5
    def testShiftLeftRow5(self):
        col = self.ran.randint(2, 7)
        new = algo.shiftLeft(5, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 4:
                    if new[i] != old[i]:
                        return False
            return new[4] == [30, 31, 32, 33, 34, 35, 29]
        self.assertTrue(check(self.seat, new))

    # to test shift left on row 6
    def testShiftLeftRow6(self):
        col = self.ran.randint(4, 5)
        new = algo.shiftLeft(6, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(5):
                if new[i] != old[i]:
                    return False
            return new[5] == [0, 0, 37, 38, 36, 0, 0]
        self.assertTrue(check(self.seat, new))

    # to test shift right on row 1
    def testShiftRightRow1(self):
        col = self.ran.randint(1, 6)
        new = algo.shiftRight(1, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(1, 6):
                if new[i] != old[i]:
                    return False
            return new[0] == [7, 1, 2, 3, 4, 5, 6]
        self.assertTrue(check(self.seat, new))

    # to test shift right on row 2
    def testShiftRightRow2(self):
        col = self.ran.randint(1, 6)
        new = algo.shiftRight(2, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 1:
                    if new[i] != old[i]:
                        return False
            return new[1] == [14, 8, 9, 10, 11, 12, 13]
        self.assertTrue(check(self.seat, new))

    # to test shift right on row 3
    def testShiftRightRow3(self):
        col = self.ran.randint(1, 6)
        new = algo.shiftRight(3, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 2:
                    if new[i] != old[i]:
                        return False
            return new[2] == [21, 15, 16, 17, 18, 19, 20]
        self.assertTrue(check(self.seat, new))

    # to test shift right on row 4
    def testShiftRightRow4(self):
        col = self.ran.randint(1, 6)
        new = algo.shiftRight(4, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 3:
                    if new[i] != old[i]:
                        return False
            return new[3] == [28, 22, 23, 24, 25, 26, 27]
        self.assertTrue(check(self.seat, new))

    # to test shift right on row 5
    def testShiftRightRow5(self):
        col = self.ran.randint(1, 6)
        new = algo.shiftRight(5, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                if i != 4:
                    if new[i] != old[i]:
                        return False
            return new[4] == [35, 29, 30, 31, 32, 33, 34]
        self.assertTrue(check(self.seat, new))

    # to test shift right on row 6
    def testShiftRightRow6(self):
        col = self.ran.randint(3, 4)
        new = algo.shiftRight(6, col, 1, self.seat.copy())

        def check(old, new):
            for i in range(5):
                if new[i] != old[i]:
                    return False
            return new[5] == [0, 0, 38, 36, 37, 0, 0]
        self.assertTrue(check(self.seat, new))

    # to test left bound
    def testLeftBound(self):
        new = algo.shiftLeft(1, 1, 1, self.seat.copy())
        self.assertEqual(self.seat, new)

    # to test right bound
    def testRightBound(self):
        new = algo.shiftRight(1, 7, 1, self.seat.copy())
        self.assertEqual(self.seat, new)

    # to test move up on col 1
    def testUpCol1(self):
        row = self.ran.randint(2, 5)
        new = algo.shiftUp(row, 1, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(1, 7):
                    if old[i][j] != new[i][j]:
                        return False
            return [new[i][0] for i in range(6)] == [8, 15, 22, 29, 1, 0]
        self.assertTrue(check(self.seat, new))

    # to test move up on col 2
    def testUpCol2(self):
        row = self.ran.randint(2, 5)
        new = algo.shiftUp(row, 2, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 1:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][1] for i in range(6)] == [9, 16, 23, 30, 2, 0]
        self.assertTrue(check(self.seat, new))

    # to test move up on col 3
    def testUpCol3(self):
        row = self.ran.randint(2, 6)
        new = algo.shiftUp(row, 3, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 2:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][2] for i in range(6)] == [10, 17, 24, 31, 36, 3]
        self.assertTrue(check(self.seat, new))

    # to test move up on col 4
    def testUpCol4(self):
        row = self.ran.randint(2, 6)
        new = algo.shiftUp(row, 4, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 3:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][3] for i in range(6)] == [11, 18, 25, 32, 37, 4]
        self.assertTrue(check(self.seat, new))

    # to test move up on col 5
    def testUpCol5(self):
        row = self.ran.randint(2, 6)
        new = algo.shiftUp(row, 5, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 4:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][4] for i in range(6)] == [12, 19, 26, 33, 38, 5]
        self.assertTrue(check(self.seat, new))

    # to test move up on col 6
    def testUpCol6(self):
        row = self.ran.randint(2, 5)
        new = algo.shiftUp(row, 6, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 5:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][5] for i in range(6)] == [13, 20, 27, 34, 6, 0]
        self.assertTrue(check(self.seat, new))

    # to test move up on col 7
    def testUpCol7(self):
        row = self.ran.randint(2, 5)
        new = algo.shiftUp(row, 7, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 6:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][6] for i in range(6)] == [14, 21, 28, 35, 7, 0]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 1
    def testDownCol1(self):
        row = self.ran.randint(1, 4)
        new = algo.shiftDown(row, 1, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(1, 7):
                    if old[i][j] != new[i][j]:
                        return False
            return [new[i][0] for i in range(6)] == [29, 1, 8, 15, 22, 0]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 2
    def testDownCol2(self):
        row = self.ran.randint(1, 4)
        new = algo.shiftDown(row, 2, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 1:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][1] for i in range(6)] == [30, 2, 9, 16, 23, 0]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 3
    def testDownCol3(self):
        row = self.ran.randint(1, 5)
        new = algo.shiftDown(row, 3, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 2:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][2] for i in range(6)] == [36, 3, 10, 17, 24, 31]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 4
    def testDownCol4(self):
        row = self.ran.randint(1, 5)
        new = algo.shiftDown(row, 4, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 3:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][3] for i in range(6)] == [37, 4, 11, 18, 25, 32]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 5
    def testDownCol5(self):
        row = self.ran.randint(1, 5)
        new = algo.shiftDown(row, 5, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 4:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][4] for i in range(6)] == [38, 5, 12, 19, 26, 33]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 6
    def testDownCol6(self):
        row = self.ran.randint(1, 4)
        new = algo.shiftDown(row, 6, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 5:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][5] for i in range(6)] == [34, 6, 13, 20, 27, 0]
        self.assertTrue(check(self.seat, new))

    # to test move down on col 7
    def testDownCol7(self):
        row = self.ran.randint(1, 4)
        new = algo.shiftDown(row, 7, 1, self.seat.copy())

        def check(old, new):
            for i in range(6):
                for j in range(7):
                    if j != 5:
                        if old[i][j] != new[i][j]:
                            return False
            return [new[i][6] for i in range(6)] == [35, 7, 14, 21, 28, 0]
        self.assertTrue(check(self.seat, new))

    # to test upper bound
    def testUpperBound(self):
        new = algo.shiftUp(1, 1, 1, self.seat.copy())
        self.assertEqual(self.seat, new)

    # to test left side lower bound
    def testLeftLowerBound(self):
        new = algo.shiftDown(5, 1, 1, self.seat.copy())
        self.assertEqual(self.seat, new)

    # to test right side lower bound
    def testRightLowerBound(self):
        new = algo.shiftDown(5, 7, 1, self.seat.copy())
        self.assertEqual(self.seat, new)

    # to test center lower bound
    def testCenterLowerBound(self):
        new = algo.shiftDown(6, 3, 1, self.seat.copy())
        self.assertEqual(self.seat, new)



if __name__ == '__main__':
    unittest.main()

