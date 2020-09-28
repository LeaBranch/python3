import os
import subprocess
import myArray as my

def copyFunc(name):
	try:
		fdr = open(name, "r")
		text = fdr.read()
		
		new_name = name.split('.')
		fin_name=new_name[0] + "(1)." + new_name[1]
		
		fdw = open(fin_name, "w")
		fdw.write(text)
		
		fdr.close()
		fdw.close()
		
	except FileNotFoundError:
		print('ошибка! файл не найден')
		print('')
	except IndexError:
		print('\nUsage: back_up <name>')
		
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
	
	choice = input("\nChoice: ")
	
	if (choice.isdigit()):
		choice = int(choice)
		if (choice == 0):
				os.chdir("..")
	# если выбранный эл-т явл. папкой
		if (os.path.isdir(list_[choice-1]) is True):
			os.chdir(list_[choice-1])
				
		# если это файл
		if (os.path.isfile(list_[choice-1])):
		#	subprocess.call(["NotePad.py", "list_[choice-1]", "-r"], shell=True)
			
			os.execl("NotePad.py",  "list_[choice-1]", "-r")
		# если это исполняемый файл(приложение)
		if (os.access(list_[choice-1], os.X_OK)):
			pass
	if (choice == "+"):
		choice = int(input("\nChoice: "))
		copyFunc(list_[choice-1])
	if (choice == "-"):
		choice = int(input("\nChoice: "))
		os.remove(list_[choice-1])
		
		
	print()
