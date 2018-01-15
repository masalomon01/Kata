# 5kyu
# chameleons is int[3], desiredColor is int from 0 to 2
def check_input(chameleons):
	check = [1 if e == 0 else 0 for e in chameleons]
	if sum(check) >= 2:
		return False


def chameleon(chameleons, desiredColor):
	desired, moves  = chameleons[desiredColor], 0
	if check_input(chameleons) == False:
		if chameleons[desiredColor]> 0:
			return 0
		else:
			return -1
	chameleons.pop(desiredColor)
	small, big = min(chameleons), max(chameleons)
	while small < big:
		small += 2
		big -= 1
		desired -= 1
		moves += 1
	if small == big:
		return small + moves
	else:
		return -1


#test.describe("All chameleons are wrong color")
print(chameleon([0, 0, 17], 1)) #, -1)
  
#test.describe("One step solution")
print(chameleon([1, 1, 15], 2)) #, 1)
  
#test.describe("Average situation")
print(chameleon([34, 32, 35], 0)) #, 35, "Wrong answer")

print(chameleon([0, 0, 0], 0)) #, 35, "Wrong answer")