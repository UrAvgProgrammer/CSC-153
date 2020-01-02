import sys, os, re
from c_lexer import imp_lex
from c_syntax_analysis import syntax_analize, parser_CST

#expected form of a C program, without line breaks
source_re = r"int main\s*\(\s*\)\s*{\s*return\s+(?P<ret>[0-9]+)\s*;\s*}" 

source_file = input("Enter file name: ")

with open(source_file, 'r') as f:
	source = f.read().strip()
	lexical_analysis = imp_lex(source)

code_to_parse = syntax_analize(lexical_analysis)

# print("\n \n \n")
# print(code_to_parse)
print(parser_CST(code_to_parse))