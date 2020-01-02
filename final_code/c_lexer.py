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
                    token = (tag, text)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

#Set 
RETURN_KEYWORD = 'RETURN_KEYWORD'
INT_KEYWORD = 'INT_KEYWORD'
MAIN_KEYWORD = 'MAIN_KEYWORD'
DECLARE = 'DECLARE'
IDENTIFIER = 'IDENTIFIER'
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
    (r'return', RETURN_KEYWORD),
    (r'int', INT_KEYWORD),
    (r'main', MAIN_KEYWORD),
    (r'[A-Za-z][A-Za-z0-9_]*', IDENTIFIER),
]

def imp_lex(characters):
    return lex(characters, token_exprs)