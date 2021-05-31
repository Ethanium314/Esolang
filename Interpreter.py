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
newpointer = Pointer(text, 200, 0, 0, 0, [1, 0])
pointers.append(newpointer)
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
		elif (this == "@"):
			pointer.value = ord(input())
		elif (this in inputs):
			pointer.value = ord(this)
		elif (this == ":"):
			print(chr(pointer.value), end="")
		elif (this == "$"):
			print(pointer.value, end="")
		elif (this == "|"):
			pointer.vector[0] = -pointer.vector[0]
		elif (this == "_"):
			pointer.vector[1] = -pointer.vector[1]
		elif (this == "?"):
			if (pointer.value != 0):
				vectadd(pointer.vector, [1, 0])
		elif (this == "!"):
			pointers.remove(pointer)
		elif (this == "*"):
			pointer.value = ord(pointer[pointer.y][pointer.x + 1])
			if (pointer.vector == [1, 0]):
				x1 += 1
				
		pointer.x += pointer.vector[0]
		pointer.y += pointer.vector[1]
		print(pointer.x)
print("")
