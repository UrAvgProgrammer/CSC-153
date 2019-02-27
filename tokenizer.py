import re

data = open('code.txt', 'r')
contents = data.read()

list_keywords = ['print', 'scanf', 'include', 'int', 'float', 'char', 'double', 'main', 'do', 'return', 'while', 'for']
list_symbols = ['#', '%', '(', ')', '{', '}', '?',  ';', '.', '_', '"', "'"]
list_operators = ['+', '/', '*', '-', '>', '<', '=', '!']
list_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
list_letters = ['A', 'a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k'\
				'L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v',\
				'W','w','X','x','Y','y','Z','z']
sym_container = []
ope_container = []
dig_container = []
words_container = []
keyword_container = []
word = []
digit = []
contents = list(contents)
for i, content in enumerate(contents):
	print str(i) + " " + str(content)
	if content in list_symbols:
		sym_container.append(content)
	elif content in list_operators:
		ope_container.append(content)
	elif content in list_letters:
		if (i+1 != len(contents)):
			if (contents[i+1] in list_letters):
				word.append(content)
			elif(contents[i+1] in list_digits):
				word.append(content)
			elif(str(contents[i+1]) == '_'):
				word.append(content)
			else:
				word.append(content)
				worded = "".join(word)
				if worded in list_keywords:
					keyword_container.append(worded)
					word[:] = []
				else:
					words_container.append(worded)
					word[:] = []
		else:
			word.append(content)	
	elif content in list_digits:
		if (i+1 != len(contents)):
			if (contents[i+1] in list_digits):
				digit.append(content)
			else:
				digit.append(content)
				digited = "".join(digit)
				dig_container.append(digited)
				digit[:] = []
		else:
			dig_container.append(content)



for w in dig_container:
	print w