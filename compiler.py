from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
from parseit import *
from lexer import *
# -------------------------------------- PARSER HERE --------------------------------------

# start: int main() { expression }

# expression : factor * | / factor ;

# factor : term + | - factor ;

# term : term | var | num ;

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

def ast(tokens):
    tokens = start(tokens)
    content = []
    for token in tokens:
        if token[0] not in ['{', '}', ';']:
            content.append(token[0])
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
        elif elem not in ['-', '+', '/', '%', '*', ')', ';']:
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
        elif elem == ';':
            pass
        else:
            print('error')
            exit()
    return pTree



data = open('code.txt', 'r')
contents = data.read()
tokens = imp_lex(contents)
# for token in tokens:
#     print(token)

parse = Parser(tokens)
parse.parse()
