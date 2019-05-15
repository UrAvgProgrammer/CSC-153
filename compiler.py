import sys
import re

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
    (r'int', RESERVED),
    (r'main', RESERVED),
    (r'[A-Za-z][A-Za-z0-9_]*', NAME),
]

def imp_lex(characters):
    return lex(characters, token_exprs)

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
                code.append(token[0])
        elif token[0] == ')':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append(token[0])
        elif token[0] == '{':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append(token[0])
        elif token[0] == '}':
            if token[0] not in start:
                start.append(token[0])
            else:
                code.append(token[0])
        else:
            code.append(token[0])
    return code


def parser(tokens):
    pass



data = open('code.txt', 'r')
contents = data.read()
tokens = imp_lex(contents)
for token in tokens:
    print (token[0])
    print (token[1])

print(start(tokens))
