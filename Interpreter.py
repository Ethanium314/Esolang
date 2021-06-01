import sys

if (sys.argv[1].split(".")[1] == "test"):
	text = open(sys.argv[1]).read()
else:
	print("invalid extension")
	quit()

class Pointer:
	def __init__(self, text, size, value, x, y, vector):
		self.value = value
		self.vector = vector
		self.x = x
		self.y = y
		
		grid = text.split("\n")
		self.grid = grid
		for i in range(len(grid)):
			while (len(grid[i]) != size):
				grid[i] += " "

def vectadd(v1, v2):
	for i in range(2):
		v1[i] += v2[i]
	return v1

pointers = []
here = 0
vec = [0, 0]
newpointer1 = Pointer(text, 200, 0, 0, 0, [1, 0])
newpointer2 = Pointer(text, 200, 0, 0, 0, [0, 1])
pointers.append(newpointer1)
pointers.append(newpointer2)
inputs = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


while (len(pointers) > 0):
	for pointer in pointers:
		this = pointer.grid[pointer.y][pointer.x]
		if (this == ">"):
			vectadd(pointer.vector, [1, 0])
		elif (this == "<"):
			vectadd(pointer.vector, [-1, 0])
		elif (this == "^"):
			vectadd(pointer.vector, [0, -1])
		elif (this == "v"):
			vectadd(pointer.vector, [0, 1])
		elif (this == ";"):
			sys.exit()
		elif (this == "+"):
			pointer.value += 1
		elif (this == "-"):
			pointer.value -= 1
		elif (this == "("):
			if(pointer.vector[0] < 0):
				pointer.vector[0] = -pointer.vector[0]
		elif (this == ")"):
			if (pointer.vector[0] > 0):
				pointer.vector[0] = -pointer.vector[0]
		elif (this == "@"):
			pointer.value = ord(input())
		elif (this == ":"):
			print(chr(pointer.value), end="")
		elif (this == "$"):
			print(pointer.value, end="")
		elif (this == "|"):
			pointer.vector[0] = -pointer.vector[0]
		elif (this == "_"):
			pointer.vector[1] = -pointer.vector[1]
		elif (this == "?"):
			if (pointer.value == ord(pointer.grid[pointer.y][pointer.x + 1])):
				#turn right
				temp = pointer.vector[0]
				pointer.vector[0] = pointer.vector[1]
				pointer.vector[1] = temp
				pointer.vector[1] = -pointer.vector[1]
			else:
				#turn left
				temp = pointer.vector[0]
				pointer.vector[0] = pointer.vector[1]
				pointer.vector[1] = temp
				pointer.vector[0] = -pointer.vector[0]
		elif (this == "!"):
			pointers.remove(pointer)
		elif (this == "*"):
			pointer.value = int(pointer.grid[pointer.y][pointer.x + 1])
			if (pointer.vector == [1, 0]):
				pointer.x += 1
		elif (this == "\""):
			pointer.value = ord(pointer.grid[pointer.y][pointer.x + 1])
			if (pointer.vector == [1, 0]):
				pointer.x += 1
		elif (this == "#"):
			if (here):
				vectadd(pointer.vector, vec)
				pointers.remove(here)
				here = 0
				vec = [0, 0]
			else:
				here = pointer
				vec = pointer.vector.copy()
				print(vec)
				pointer.vector = [0, 0]
				
		pointer.x += pointer.vector[0]
		pointer.y += pointer.vector[1]
		#print(pointer.vector)
		#print(pointer.x, pointer.y)
		#print(vec)
		#print(pointer.x, pointer.y)
	#here = 0
	print("\n")
print("")
