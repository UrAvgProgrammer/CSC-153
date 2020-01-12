import ply.lex as lex
import ply.yacc as yacc

tokens = ['NAME', 'NUMBER', 'ADD', 'SUB', 'MULT', 'DIV', 'EQUAL', 'END_ST', 'OPEN_PAR', 'CLOSE_PAR', 'OPEN_CURL', 'CLOSE_CURL']

t_ignore = ' \t \n'
t_NAME = r'[a-zA-Z][a-zA-z0-9_]*'
t_ADD = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_EQUAL = r'='
t_END_ST = r';'
t_OPEN_PAR = r'\('
t_CLOSE_PAR = r'\)'
t_OPEN_CURL = r'{'
t_CLOSE_CURL = r'}'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def p_assign(p):
    '''assign : NAME EQUAL expr END_ST'''
    p[0] = ('ASSIGN',p[1],p[3])
def p_expr_add(p):
    '''expr : expr ADD term 
    | OPEN_PAR expr ADD term CLOSE_PAR'''
    p[0] = ('+',p[1],p[3])
def p_expr_sub(p):
    '''expr : expr SUB term 
    | OPEN_PAR expr SUB term CLOSE_PAR'''
    p[0] = ('-',p[1],p[3])
def p_term_mul(p):
    '''term : term MULT factor 
    | OPEN_PAR expr MULT factor CLOSE_PAR'''
    p[0] = ('*',p[1],p[3])
def p_term_div(p):
    '''term : term DIV factor 
    | OPEN_PAR expr DIV factor CLOSE_PAR'''
    p[0] = ('/',p[1],p[3])
def p_unit(p):
    '''expr : term 
       term : factor
    '''
    p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER'''
    p[0] = ('NUM',p[1])


def prep(tokens):
    code = []
    tok_stream = []
    for token in tokens:
        code.append(token[0])

    for cont in code:
        if cont not in ['(', ')']:
            tok_stream.append(cont)
    contents =  ' '.join(tok_stream)
    ast(contents)

def ast(contents):
    lex.lex()
    print(contents)
    # print(contents)
    # data = open('code.txt', 'r')
    # contents = data.read()

    lex.input(contents)

    while True:
        tok = lex.token()
        print(tok)
        # print(tok)
        if not tok: break

    tok = lex.token()
    print(tok)
    # print(tok)

    yacc.yacc() 
    t = yacc.parse(contents)

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
    # if len(start) != 6:
    #   print('Syntax error')
    #   quit()
    return code
