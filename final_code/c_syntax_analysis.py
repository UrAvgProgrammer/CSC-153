import sys

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval:
            self.stack.append(dataval)
            return True
        else:
            return False

    def elem(self):
        for x in self.stack:
            print (x)
        return self.stack

    def len(self):
    	return len(self.stack)

    def peek(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack[len(self.stack) - 1]
    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


def syntax_analize(contents):
    token_stack = Stack()
    code_in_main = []
    for content in contents:
        if token_stack.len() != 0:
            if content[0] != 'OPEN_CURL' and content[0] != 'CLOSE_CURL':
                code_in_main.append(content)
        if content[0] == 'OPEN_CURL':
            token_stack.add(content)
        elif content[0] == 'CLOSE_CURL':
            token_stack.remove()

    if token_stack.len() != 0:
        print('Syntax Error missing { or }')
        sys.exit()
    return code_in_main

def parser_CST(contents):
    to_parse = []
    sub_st = []
    for content in contents:
        sub_st.append(content)
        if content[0] == 'END_ST':
            to_parse.append(sub_st.copy())
            sub_st *= 0
    return to_parse

