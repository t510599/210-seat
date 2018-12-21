# -*- coding: utf-8 -*-
from algo import generateSeats, printArr, shiftUp, shiftDown, shiftLeft, shiftRight, shiftLeftDown, shiftLeftUp, shiftRightDown, shiftRightUp
from pymongo import MongoClient
from random import choice
import sys
import json

def load():
    with open('seats.txt','r',encoding="utf-8") as f:
        seats = json.load(f)
    return seats

def save(seats):
    with open('seats.txt','w',encoding="utf-8") as n:
        n.write(str(seats))

def query():
    client = MongoClient('127.0.0.1', 27017)
    db = client['210-seats']
    collection = db['users']

    data = collection.find().sort("no", )
    for user in data:
        yield user

def apply_requirements(seats, requirements):
    funcs = {"f": shiftUp,"b": shiftDown, "l": shiftLeft, "r": shiftRight, "fr": shiftRightUp, "br": shiftRightDown, "fl": shiftLeftUp, "bl": shiftLeftDown} # f: forward, b: backward, l:left, r: right
    name = {"f": "Forward","b": "Backward", "l": "Left", "r": "Right", "fr": "Right Forward", "br": "Right Backward", "fl": "Left Forward", "bl": "Left Backward"}
    order = sorted([int(n) for n in requirements.keys()])
    luckier = choice(order)
    print("Luckier: " + str(luckier) + "\n")
    order = order[order.index(luckier):] + order[:order.index(luckier)]

    for req in order:
        no, direction, steps = requirements[str(req)]
        row,col = find(seats, no)
        if col != None and row != None:
            if direction in funcs.keys():
                funcs[direction](row, col, steps, seats)
                print(no, name[direction], steps)
                printArr(seats)
                print()
    return seats

def find(seats, no, raw=False):
    if raw:
        modifier = 0
    else:
        modifier = 1 # start from 0 -> start from 1

    for y in range(len(seats)):
        if no in seats[y]:
            col = seats[y].index(no)
            row = y
            return (row + modifier, col + modifier)
    return (None,None)

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
            seats = generateSeats()
            printArr(seats)
            save(seats)
            print("Done!")
        elif mode == "run" or mode == "debug":
            seats = load()
            print("Original:")
            printArr(seats)

            # load requirements
            requirements = dict()
            with open('requirements.txt', 'w', encoding="utf-8") as req_f:
                for user in query():
                    if user['steps'].strip() != "":
                        requirements[str(user['no'])] = (user['no'], user['direction'], int(user['steps']))
                        req_f.write("{0} {1} {2}\n".format(user['no'], user['direction'], int(user['steps'])))
            
            apply_requirements(seats, requirements)

            print("Result:")
            printArr(seats)

            # save
            if mode == "run":
                with open('seats.txt','w',encoding="utf-8") as n:
                    n.write(str(seats))

            print("Done!")
        elif mode == "switch":
            seats = load()

            one = int(sys.argv[2])
            two = int(sys.argv[3])
            pos_one = find(seats, one, True)
            pos_two = find(seats, two, True)
            seats[pos_one[0]][pos_one[1]], seats[pos_two[0]][pos_two[1]] = seats[pos_two[0]][pos_two[1]], seats[pos_one[0]][pos_one[1]]

            printArr(seats)
            save(seats)

            # logging switch
            log = open('switch.txt','a',encoding='utf-8')
            log.write("{} {}\n".format(str(one), str(two)))
            log.close()
        elif mode == "export":
            requirements = dict()
            with open('requirements.txt', 'w', encoding="utf-8") as req_f:
                for user in query():
                    if user['steps'].strip() != "":
                        requirements[str(user['no'])] = (user['no'], user['direction'], int(user['steps']))
                        req_f.write("{0} {1} {2}\n".format(user['no'], user['direction'], int(user['steps'])))

            print(requirements)
        elif mode == "print":
            printArr(load())
        else:
            print(help_msg)
            sys.exit(1)
