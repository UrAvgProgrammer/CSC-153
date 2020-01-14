import sys, os, re
from c_lexer import imp_lex
from c_syntax_analysis import syntax_analize, parser_CST
from Ast import prep
from ast_lexer import imp_lex as imp_lex2
from ast_start import start
from cst import CST

sys.setrecursionlimit(10000)

#expected form of a C program, without line breaks
source_re = r"int main\s*\(\s*\)\s*{\s*return\s+(?P<ret>[0-9]+)\s*;\s*}" 

source_file = "code.c"

with open(source_file, 'r') as f:
	source = f.read().strip()
	lexical_analysis = imp_lex(source)

code_to_parse = syntax_analize(lexical_analysis)

## To run CST codes here!!

cst = CST(code_to_parse)
cst.start()
print('CST')
cst.print_tree()

#
# To run AST codes here
#

print('\nAST')

data = open("code.c", 'r')
contents = data.read()
tokens = imp_lex2(contents)
prep(start(tokens))

