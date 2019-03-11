import pprint
storage = []
key = []
value = []
token = []
datatypes = ["int", "double", "float"]
symbols = ['+', '-', '*', '/', ';', ':', '{', '}', '[', ']', '(', ')', '#', '=', '==', '!=']
reserve = ['return', 'main', 'void', '#include', 'include', 'stdio.h', '<stdio.h>', 'scanf', 'printf', 'printf(', 'if', 'else', 'elif']
def detect(storage):
	stack = []
	for i in storage:
		if  type(i) == list:
			key.append(type(i))
			value.append(i)
		elif i in datatypes:
			key.append("datatype")
			value.append(i)
		elif i in reserve:
			key.append("reserve")
			value.append(i)
		elif i.isdigit():
			key.append("digit")
			value.append(i)
		elif i in symbols:
			key.append("symbol")
			value.append(i)
		elif  i.isalpha():
			key.append("identifier")
			value.append(i)
def store():
	fname = raw_input("enter the text file: ")
	f =  open(fname,'rb')
	for line in  f:
		splits = line.split()
		for i in splits:
			storage.append(i)

def token_disp(key,value):
	i = 0
	while(i != len(key)):
		token.append('('+key[i]+','+str(i)+')')		
		i+=1
	pprint.pprint(token)

def checker():
	index = input("\nenter index: ")
	print str(key[index]) + " == " + str(value[index])

store()
detect(storage)
token_disp(key,value)
rep = True
while(rep):
	checker()
	response = raw_input("want to try again?(y/n) ")
	if response == 'n':
		print "bye~~ :*"
		rep = False
	elif response == 'y':
		pass
	else:
		print "wrong input"
