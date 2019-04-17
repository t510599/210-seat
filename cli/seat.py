# -*- coding: utf-8 -*-
from algo import generateSeats, printArr, shiftUp, shiftDown, shiftLeft, shiftRight, shiftLeftDown, shiftLeftUp, shiftRightDown, shiftRightUp
from pymongo import MongoClient
from random import choice
import sys
import json

class Seat():
    def __init__(self, seats=[]):
        if len(seats) == 0:
            self.seats = self.load()
            self.requirements = self.load_requirements()
        else:
            self.seats = seats
            self.requirements = self.load_requirements()

    def load(self):
        with open('seats.txt', 'r', encoding="utf-8") as f:
            seats = json.load(f)
        return seats
    
    def load_requirements(self):
        req = dict()
        with open('requirements.txt', 'w', encoding="utf-8") as req_f:
            for user in self.query():
                if user['steps'].strip() != "":
                    req[str(user['no'])] = (user['no'], user['direction'], int(user['steps']))
                    req_f.write("{0} {1} {2}\n".format(user['no'], user['direction'], int(user['steps'])))
        return req

    def save(self):
        with open('seats.txt','w',encoding="utf-8") as n:
            n.write(str(self.seats))

    def query(self):
        client = MongoClient('127.0.0.1', 27017)
        db = client['210-seats']
        collection = db['users']

        data = collection.find().sort("no", )
        for user in data:
            yield user

    def find(self, no, raw=False):
        if raw:
            modifier = 0
        else:
            modifier = 1 # start from 0 -> start from 1

        for y in range(len(self.seats)):
            if no in self.seats[y]:
                col = self.seats[y].index(no)
                row = y
                return (row + modifier, col + modifier)
        return (None,None)

    def switch(self, one, two):
        # one: the first person; two: the second person
        pos_one = self.find(one, True)
        pos_two = self.find(two, True)
        self.seats[pos_one[0]][pos_one[1]], self.seats[pos_two[0]][pos_two[1]] = self.seats[pos_two[0]][pos_two[1]], self.seats[pos_one[0]][pos_one[1]]

        # logging switch
        with open('switch.txt','a',encoding='utf-8') as log:
            log.write("{} {}\n".format(str(one), str(two)))

        return ((one, pos_two), (two, pos_one)) # return the result

    def apply_requirements(self):
        funcs = {"f": shiftUp, "b": shiftDown, "l": shiftLeft, "r": shiftRight, "fr": shiftRightUp, "br": shiftRightDown, "fl": shiftLeftUp, "bl": shiftLeftDown} # f: forward, b: backward, l:left, r: right
        name = {"f": "Forward", "b": "Backward", "l": "Left", "r": "Right", "fr": "Right Forward", "br": "Right Backward", "fl": "Left Forward", "bl": "Left Backward"}

        order = sorted([int(n) for n in self.requirements.keys()])
        luckier = choice(order)
        print("Luckier: " + str(luckier) + "\n")
        order = order[order.index(luckier):] + order[:order.index(luckier)]

        for req in order:
            no, direction, steps = self.requirements[str(req)]
            row, col = self.find(no)
            if col != None and row != None:
                if direction in funcs.keys():
                    funcs[direction](row, col, steps, self.seats)
                    print(no, name[direction], steps)
                    printArr(self.seats)
                    print()
        return self.seats


help_msg = '''Please provide mode!
generate - generate a random seat
switch <no1> <no2> - switch seats of two students
run - apply requirements
export - export requirements to requirements.txt
print - print the current seat
debug - dry run'''

if __name__ == "__main__":
    if len(sys.argv) <= 1 or sys.argv[1] == "help":
        print(help_msg)
        sys.exit(1 if len(sys.argv) <= 1 else 0)
    else:
        mode = sys.argv[1]
        if mode == "generate":
            seats = Seat(generateSeats())
            printArr(seats.seats)
            seats.save()
            print("Done!")
        elif mode == "run" or mode == "debug":
            seats = Seat()
            print("Original:")
            printArr(seats.seats)
            
            seats.apply_requirements()

            print("Result:")
            printArr(seats.seats)

            # save
            if mode == "run":
                seats.save()

            print("Done!")
        elif mode == "switch":
            seats = Seat()

            one = int(sys.argv[2])
            two = int(sys.argv[3])
            result = seats.switch(one, two)
            for i in result:
                print("{} postion {}".format(i[0], i[1]))

            printArr(seats.seats)
            seats.save()
        elif mode == "export":
            seats = Seat()
            print(seats.requirements)
        elif mode == "print":
            seats = Seat()
            printArr(seats.seats)
        else:
            print(help_msg)
            sys.exit(1)