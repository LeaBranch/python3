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
with open(name_f) as f:
	file = f.readlines()
#file.append('\n')

o = ["if", "elif", "else", "while", "for", "def", "with"]
countSpace = 0
countSpace_new = 0
con = 2
check = 0

for i in range(len(file)):
	n=i+1
	if(i==len(file)-1): n=i
	
	# считаем сколько по факту пробелов
	check = myCountFunc(file[i], " ")
	
	
	# считаем нужное количество пробелов
	for t in range(len(o)):
		mult = file[i].count(o[t])
		if(mult == 1):
			#print('mult: ', o[t])
			countSpace += 1
			countSpace_new = con * countSpace	
		if(mult > 1):
			countSpace += 2
			countSpace_new = con + countSpace
			
			#print(i+1, "  check: ", check, "countSpace_new: ", countSpace_new)
					
			# сравниваем
	if (check == countSpace_new):
		print("ok!")
	elif (check < countSpace_new):
		print("bad: not enough\n")
	elif (check > countSpace_new):
		print("bad: many spaces\n")
print(i+1, "  check: ", check, "countSpace_new: ", countSpace_new)
