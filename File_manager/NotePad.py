import sys

def readFunc(name):
	s = 0
	s = open(name,'r')
	print(s.read())
	s.close()
	
def writeFunc(name):
	s = 0
	s = open(name, 'w')
	text = input("Enter: ")
	s.write(text)
	s.close()

def w_endFunc(name):
	s = 0
	s = open(name, 'a')
	text = input("Enter: ")
	s.write(text)
	s.close()

def r_lineFunc(name):
	s = 0
	s = open(name)
	while(1):
		print(s.readline())
		q = input()
		if(q == ' '):
			continue
		if(q == 'exit'):
			break
	s.close()

def w_lineFunc(name)
	l = input('?:' )
	
	s = open(name)
	fd = s.readlines()
	write(fd)
	
	s.close()


#ввод файла
try:
	name = sys.argv[1]
	flag = sys.argv[2]
	
	if(flag == '-r'):
		readFunc(name)
	if(flag == '-w'):
		writeFunc(name)
	if(flag == '-e'):
		w_endFunc(name)
	if(flag == '-rl'):
		r_lineFunc(name)
	if(flag == '-wl'):
		w_lineFunc(name)
		
except FileNotFoundError:
	print('ошибка! файл не найден')
	print('')
except IndexError:
	print('\nUsage: notepad <name> <flags>\n\n-w  write\n-r  read\n-e  write to end\n')



# to do:
# \/ открыть файл (с помощью with as)
# \/ записать неск строк текста
# \/закрыть
# \/ открыть и прочитать
# \/ закрыть

# выбор:
#\/w - перезапись
#\/r - чтение 
#\/e - запись в конец
#\/rl - чтение строки
#wl - запись строки