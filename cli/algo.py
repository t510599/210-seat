from random import randrange

'''
Original from secminhr
modified by t510599
'''

# init seats
def generateSeats():
	seats = []
	numbers = [i for i in range(1, 39)]
	for i in range(6):
		seats.append([])
		for j in range(7):
			seats[len(seats)-1].append(0)
			if i == 5:
				if 0<=j<=1 or 5<=j<= 6:
					continue
			index = randrange(0, 38)
			while(numbers[index] == 0):
				index = randrange(0, 38)
			seats[i][j] = numbers[index]
			numbers[index] = 0
	return seats

# print seats
def printArr(seats):
	for i in range(len(seats)):
		for j in range(len(seats[0])):
			num = seats[i][j]
			if 0 <= num <= 9:
				num = '0' + str(num)
			print(num, end=" ")
		print()
	print() # newline

def _arrShiftLeft(index, arr, num):
	element = arr[index]
	zero_index = []
	while 0 in arr:
		index = arr.index(0)
		zero_index += [index]
		del arr[index]
	zero_index = zero_index[::-1]
	index = arr.index(element)
	if num > index:
		num = index
	front_list = arr[:num]
	arr = arr[num:len(arr)] + front_list
	
	for i in zero_index:
		arr.insert(i, 0)
	return arr

def _arrShiftRight(index, arr, num):
	element = arr[index]
	zero_index = []
	while 0 in arr:
		index = arr.index(0)
		zero_index += [index]
		del arr[index]
	zero_index = zero_index[::-1]
	index = arr.index(element)
	if num > len(arr) - index - 1:
		num = len(arr) - index - 1
	later_list = arr[len(arr) - num:len(arr)]
	arr = later_list + arr[:len(arr)-num] 
	for i in zero_index:
		arr.insert(i, 0)
	return arr


######### Actions ############

def shiftRight(row, col, num, seats):
	row_list = seats[row - 1]
	row_list = _arrShiftRight(col - 1, row_list, num)
	seats[row - 1] = row_list
	return seats

def shiftLeft(row, col, num, seats):
	row_list = seats[row - 1]
	row_list = _arrShiftLeft(col - 1, row_list, num)
	seats[row - 1] = row_list
	return seats

def shiftUp(row, col, num, seats):
	col_list = [seats[i][col - 1] for i in range(len(seats))]
	col_list = _arrShiftLeft(row - 1 ,col_list, num)
	for i in range(len(seats)):
		seats[i][col - 1] = col_list[i]
	return seats

def shiftDown(row, col, num, seats):
	col_list = [seats[i][col - 1] for i in range(len(seats))]
	col_list = _arrShiftRight(row - 1 ,col_list, num)
	for i in range(len(seats)):
		seats[i][col - 1] = col_list[i]
	return seats

# get list of element from left bottom to right top
def _getUpperCross(row, col, arr):
	target_list = []
	current_row = row
	current_col = col
	highest_pos = (0, 0)
	#get all right up corner
	while current_row >= 1 and current_col <= len(arr[0]):
		target_list.insert(0, arr[current_row-1][current_col-1])
		current_row -= 1
		current_col += 1
	highest_pos = (current_row + 1, current_col - 1)
	current_row = row + 1
	current_col = col  - 1
	#get all left bottom corner
	while current_row <= len(arr) and current_col >= 1:
		target_list.append(arr[current_row-1][current_col-1])
		current_row += 1
		current_col -= 1
	return (target_list, highest_pos)

# get list of element from left top to right bottom
def _getLowerCross(row, col, arr):
	target_list = []
	current_row = row
	current_col = col
	highest_pos = (0, 0)
	#get all left up corner
	while current_row >= 1 and current_col >= 1:
		target_list.insert(0, arr[current_row-1][current_col-1])
		current_row -= 1
		current_col -= 1
	highest_pos = (current_row + 1, current_col + 1)
	current_row = row + 1
	current_col = col + 1
	#get all right down corner
	while current_row <= len(arr) and current_col <= len(arr[0]):
		target_list.append(arr[current_row-1][current_col-1])
		current_row += 1
		current_col += 1
	return (target_list, highest_pos)

def shiftRightUp(row, col, num, seats):
	# the list is follows the predicate: n.row > (n+1).row
	corner_list, highest_pos = _getUpperCross(row, col, seats)
	target = seats[row-1][col-1]
	corner_list = _arrShiftLeft(corner_list.index(target) ,corner_list, num)
	#fill in 
	current_row = highest_pos[0]
	current_col = highest_pos[1]
	while corner_list:
		seats[current_row-1][current_col-1] = corner_list[0]
		del corner_list[0]
		current_row += 1
		current_col -= 1
	return seats

def shiftRightDown(row, col, num, seats):
	# the list is follows the predicate: n.row > (n+1).row
	corner_list, highest_pos = _getLowerCross(row, col, seats)
	target = seats[row-1][col-1]
	corner_list = _arrShiftRight(corner_list.index(target) ,corner_list, num)
	#fill in 
	current_row = highest_pos[0]
	current_col = highest_pos[1]
	while corner_list:
		seats[current_row-1][current_col-1] = corner_list[0]
		del corner_list[0]
		current_row += 1
		current_col += 1
	return seats

def shiftLeftUp(row, col, num, seats):
	corner_list, highest_pos = _getLowerCross(row, col, seats)
	target = seats[row-1][col-1]
	corner_list = _arrShiftLeft(corner_list.index(target) ,corner_list, num)
	#fill in 
	current_row = highest_pos[0]
	current_col = highest_pos[1]
	while corner_list:
		seats[current_row-1][current_col-1] = corner_list[0]
		del corner_list[0]
		current_row += 1
		current_col += 1
	return seats

def shiftLeftDown(row, col, num, seats):
	corner_list, highest_pos = _getUpperCross(row, col, seats)
	target = seats[row-1][col-1]
	corner_list = _arrShiftRight(corner_list.index(target) ,corner_list, num)
	#fill in 
	current_row = highest_pos[0]
	current_col = highest_pos[1]
	while corner_list:
		seats[current_row-1][current_col-1] = corner_list[0]
		del corner_list[0]
		current_row += 1
		current_col -= 1
	return seats