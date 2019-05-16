class Parser(object):

	def __init__(self, tokens):
		self.tokens = tokens
		self.token_index = 0

	def parse(self):

		while self.token_index < len(self.tokens):
			token_value = self.tokens[self.token_index][0]
			token_type = self.tokens[self.token_index][1]
			
			if token_type == 'DECLARE' and token_value == 'int':
				self.p_declare(self.tokens[self.token_index:len(self.tokens)])
			elif token_type == 'IDENTIFIER':
				pass# self.p_assign(self.tokens[self.token_index:len(self.tokens)])
			self.token_index += 1

	#declare : type identifier equal (number | identifier)	
	def p_declare(self, token_s):
		tokens_checked = 0

		for token in range(0, len(token_s)):
			print(token_s[token])
			token_value = token_s[tokens_checked][0]
			token_type = token_s[tokens_checked][1]

			if token_type == 'END_ST':
				break

			if token == 0:
				print('variable type: ', token_value)
			elif token == 1 and token_type == 'IDENTIFIER':
				print('variable name: ', token_value)
			elif token == 1 and token_type != 'IDENTIFIER':
				print('ERROR: Invalid var name: ', token_value)
				quit()

			elif token == 2 and token_type == 'EQUAL':
				print('assignment operator: ', token_value)
			elif token == 2 and token_type != 'EQUAL':
				print('ERROR: Invalid assignment operator is missing or invalid operator: ')
				quit()

			elif token == 3 and token_type in ['IDENTIFIER', 'NUMBER']:
				print('variable value: ', token_value)
			elif token == 3 and token_type not in ['IDENTIFIER', 'NUMBER']:
				print('ERROR: invalid value')
				quit()

			tokens_checked += 1

