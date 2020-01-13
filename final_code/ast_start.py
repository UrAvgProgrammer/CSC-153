
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

class Parser(object):

	def __init__(self, tokens):
		self.tokens = tokens
		self.pos = 0
		self.current_token = None
		self.token_value = self.tokens[self.pos][0]
		self.token_type = self.tokens[self.pos][1]

	def advance(self):
		self.pos +=1
		if self.pos > len(self.tokens):
			self.token_value = None  # Indicates end of input
		else:
			self.token_value = self.tokens[self.pos][0]

	def parse(self, token_type):
		if self.token_type == token_type:
			self.current_token = self.token_value


	def factor(self):
		pass

def start(tokens):
    code = []
    start = []
    for token in tokens:
        if token[0] == 'int':
            start.append(token[0])
        elif token[0] == 'main':
            start.append(token[0])
        elif token[0] == '(':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append((token))
        elif token[0] == ')':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append((token))
        elif token[0] == '{':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append((token))
        elif token[0] == '}':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append((token))
        else:
            code.append((token))
    return code

