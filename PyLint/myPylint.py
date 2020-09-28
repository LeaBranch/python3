import sys

#class Error:
#	colon

argc = len(sys.argv)
# получение имени файла
if (argc != 2):
	print('Usage: ' + sys.argv[0] +  ' <filename>')
	exit(1)

name_p = sys.argv[0]
name_f = sys.argv[1]

# открытие и чтение кода
file = open(name_f, "r")
brackedOpen = 0
brackedClosed = 0
o = ["if", "elif", "else", "while", "for", "def"]
d = 0
con = "    "

for line in file:
# Е-01
	# if ("if" in line) and (':' not in line):
	#		print("Error!")

# E-02

	for t in range(len(o)):
		mult = line.count(o[t])
		if(mult>0):
			#print('mult: ', o[t])
			d += 1
			
			
		
# Е-03
	brackedOpen += line.count("(")
	brackedClosed += line.count(")")
if (brackedOpen != brackedClosed):
	print("Error! ()")

file.close()
