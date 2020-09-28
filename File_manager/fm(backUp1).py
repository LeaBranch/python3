import os
import myArray as my

def Head(flag):
	path = os.getcwd()
	if flag == 1:
		return (path + "\n")
	else:
		tmp = os.path.split(path)
		return ("\t\t" + tmp[1])

while(1):
	# вывод назв. директ / пути
	print(Head(0))
	print("=="*15 + "\n")

	# вывод списка файлов
	list_ = os.listdir()
	print("[ 0 ] ..")
	my.out2(list_)
	
	choice = int(input("\nChoice: "))
	# если выбранный эл-т явл. папкой
	if (os.path.isdir(list_[choice-1]) is True):
		if (choice == 0):
			os.chdir("..")
		else:
			os.chdir(list_[choice-1])
	# если это файл
	if (os.path.isfile(list_[choice-1])):
		print("\nisFile\n")
	# если это исполняемый файл(приложение)
	if (os.access(list_[choice-1], os.X_OK)):
		pass
	print()
