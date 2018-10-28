from algo import generateSeats, printArr, shiftUp, shiftDown, shiftLeft, shiftRight, shiftLeftDown, shiftLeftUp, shiftRightDown, shiftRightUp
from random import choice
import sys
import json

def load():
    f = open('seats.txt','r',encoding="utf-8")
    seats = json.load(f)
    f.close()
    return seats

def parse(seats,requirements):
    funcs = {"f": shiftUp,"b": shiftDown, "l": shiftLeft, "r": shiftRight, "fr": shiftRightUp, "br": shiftRightDown, "fl": shiftLeftUp, "bl": shiftLeftDown} # f: forward, b: backward, l:left, r: right
    name = {"f": "向前","b": "向後", "l": "向左", "r": "向右", "fr": "向右前", "br": "向右後", "fl": "向左前", "bl": "向左後"}
    order = sorted([int(n) for n in requirements.keys()])
    luckier = choice(order)
    print("幸運兒: " + str(luckier) + "\n")
    order = order[order.index(luckier):] + order[:order.index(luckier)]

    for req in order:
        no,direction,steps = requirements[str(req)]
        no = no
        steps = steps
        row,col = find(seats,no)
        if col != None and row != None:
            if direction in funcs.keys():
                funcs[direction](row,col,steps,seats)
                print(no, name[direction], steps)
                printArr(seats)
                print()
    return seats

def find(seats,no):
    for y in range(len(seats)):
        if no in seats[y]:
            col = seats[y].index(no)
            row = y
            return (row+1,col+1) # start from 0 -> start from 1
    return (None,None)

help_msg = '''Please provide mode!
generate - generate a random seat
run - apply requirements
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
            n = open('seats.txt','w',encoding="utf-8")
            n.write(str(seats))
            n.close()
            print("Done!")
        elif mode == "run" or mode == "debug":
            seats = load()
            print("Original:")
            printArr(seats)
            #load requirements
            requirements = dict()
            r = open('requirements.txt','r',encoding="utf-8")
            for line in r.readlines():
                no,direction,steps = line.strip().split(" ")
                requirements[no] = (int(no),direction,int(steps))
            parse(seats,requirements)
            print("Result:")
            printArr(seats)
            if mode == "run":
                #save
                n = open('seats.txt','w',encoding="utf-8")
                n.write(str(seats))
                n.close()
            print("Done!")
        elif mode == "show":
            printArr(load())
        else:
            print(help_msg)
            sys.exit(1)
