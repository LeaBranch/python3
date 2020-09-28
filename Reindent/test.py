import sys

def myCountFunc(str, lec):
	s = 0
	for i in range(len(str)):
		if (str[i] == lec):
			s += 1
		else: break
	return s


argc = len(sys.argv)
# получение имени файла
if (argc != 2):
	print('Usage: ' + sys.argv[0] +  ' <filename>')
	exit(1)

name_p = sys.argv[0]
name_f = sys.argv[1]

# открытие и чтение кода
file = open(name_f, "r")
o = ["if", "elif", "else", "while", "for", "def"]
countSpace = 0
countSpace_new = 0
con = 2
check = 0
i=0
n=0

for line in file:
	n=i+1
	
	# считаем сколько по факту пробелов
	#check = line.count(" ")
	check = myCountFunc(line.index(n), " ")
	print("countSpace_new: ", countSpace_new, "check: ", check)
	
	# считаем нужное количество пробелов
	for t in range(len(o)):
		mult = line.count(o[t])
		if(mult>0):
			print('mult: ', o[t])
			countSpace += 1
			countSpace_new = con * countSpace	
			
	# сравниваем
	if (check == countSpace_new):
		print("ok!")
	elif (check < countSpace_new):
		print("bad: not enough\n")
	elif (check > countSpace_new):
		print("bad: many spaces\n")
	i+=1
