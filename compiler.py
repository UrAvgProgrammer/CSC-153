import sys
import re
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


RESERVED = 'RESERVED'
NAME = 'NAME'
OPEN_PAR = 'OPEN_PAR'
CLOSE_PAR = 'CLOSE_PAR'
OPEN_CURL = 'OPEN_CURL'
CLOSE_CURL = 'CLOSE_CURL'
EQUAL = 'EQUAL'
ADD = 'ADD'
SUB = 'SUB'
MUL = 'MUL'
DIV = 'DIV'
NUMBER = 'NUMBER'
END_ST = 'END_ST'

token_exprs = [
    (r'[ \n\t]+', None),
    (r'#[^\n]*', None),
    (r'\(', OPEN_PAR),
    (r'\)', CLOSE_PAR),
    (r';', END_ST),
    (r'\+', ADD),
    (r'-',  SUB),
    (r'\*', MUL),
    (r'/', DIV),
    (r'=', EQUAL),
    (r'{', OPEN_CURL),
    (r'}', CLOSE_CURL),
    (r'[0-9]+', NUMBER),
    (r'[A-Za-z][A-Za-z0-9_]*', NAME),
]

def imp_lex(characters):
    return lex(characters, token_exprs)

# -------------------------------------- PARSER HERE --------------------------------------

# class Stack:

#     def __init__(self):
#         self.stack = []

#     def add(self, dataval):
# # Use list append method to add element
#         if dataval:
#             self.stack.append(dataval)
#             return True
#         else:
#             return False
#     def elem(self):
#         for x in self.stack:
#             print (x)

#     def len(self):
#         return len(self.stack)
# # Use list pop method to remove element
#     def remove(self):
#         if len(self.stack) <= 0:
#             return ("No element in the Stack")
#         else:
#             return self.stack.pop()

def parser(tokens):
    pass

def AST(tokens):
    content = []
    for token in tokens:
        content.append(token[0])
    # content = list(content)
    # content = content.split()
    print(content)
    treeStack = Stack() #to keep track the parent node
    pTree = BinaryTree('') #Initialize empty tree
    treeStack.push(pTree)
    currentNode = pTree
    for elem in content:
        if elem == '(':
            currentNode.insertLeft('')
            treeStack.push(currentNode)
            currentNode = currentNode.getLeftChild()
        elif elem not in ['-', '+', '/', '%', '*', ')']:
            currentNode.setRootVal(elem)
            parentNode = treeStack.pop()
            currentNode = parentNode
        elif elem in ['-', '+', '/', '%', '*']:
            currentNode.setRootVal(elem)
            currentNode.insertRight('')
            treeStack.push(currentNode)
            currentNode = currentNode.getRightChild()
        elif elem == ')':
            currentNode = treeStack.pop()
        else:
            print('error')
            exit()
    return pTree

data = open('code.txt', 'r')
contents = data.read()
tokens = imp_lex(contents)
for token in tokens:
    print (token[0])
    print (token[1])

print(AST(tokens))
