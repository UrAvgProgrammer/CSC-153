from anytree import Node, RenderTree

class CST():
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.assign_head = None
        self.data_name = None
        self.data_value = None
        self.expr = []
        self.root = Node("Prog")
        self.current_head = self.root
        self.current_token = self.tokens[self.pos]
        self.div_parent = None
        self.mul_parent = None
        self.add_parent = None
        self.div_parent = None


    def step(self):
        self.move_pos()
        self.next_token()

    def move_pos(self):
        self.pos = self.pos + 1

    def next_token(self):
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def start(self):
        if self.has_next():
            if self.current_token[0] == 'IDENTIFIER':
                if self.tokens[self.pos + 1][0] == 'EQUAL': 
                    self.assign()
            elif self.current_token[0] == 'END_ST':
                if self.has_next():
                    self.current_head = self.root
                    return self.assign()
                else:
                    data_name = Node('END_ST', parent = self.current_head)
                    assign = Node(';', parent = data_name)
                    exit()
            else:
                return self.expression()

    def has_next(self):
        if self.pos <= len(self.tokens)-1 and self.tokens[self.pos+1][0] != 'END_ST':
            return True
        return False

    def expression(self):
        term1 = self.term()

        while self.current_token[0] in ['ADD', 'SUB']:
            if self.current_token[0] == 'ADD':
                local_head = Node('ADD', parent = self.current_head)

                term1.parent = local_head
                
                data_name = Node('operation', parent = local_head)
                data_value = Node(self.current_token[1], parent = data_name)

                self.step()
                
                term1 = self.expression()
                term1.parent = local_head

                self.step()
                term1 = local_head
            else:
                local_head = Node('SUB', parent = self.current_head)

                term1.parent = local_head
                

                data_name = Node('operation', parent = local_head)
                data_value = Node(self.current_token[1], parent = data_name)

                
                self.step()
               
                term1 = self.expression()
                term1.parent = local_head

                self.step()
                term1 = local_head
        return term1

    def term(self):
        factor1 = self.factor()

        while self.current_token[0] in ['MUL', 'DIV']:
            if self.current_token[0] == 'MUL':
                local_head = Node('MUL', parent = self.current_head)

                factor1.parent = local_head
                
                data_name = Node('operation', parent = local_head)
                data_value = Node(self.current_token[1], parent = data_name)

                self.step()
                
                factor1 = self.expression()
                factor1.parent = local_head

                self.step()
                factor1 = local_head
            else:
                local_head = Node('DIV', parent = self.current_head)

                factor1.parent = local_head
                

                data_name = Node('operation', parent = local_head)
                data_value = Node(self.current_token[1], parent = data_name)

                
                self.step()
               
                factor1 = self.expression()
                factor1.parent = local_head

                self.step()
                factor1 = local_head

        return factor1


    def factor(self):

        if self.current_token[0] in ['NUMBER', 'IDENTIFIER']:
            if self.has_next():
                local_head = Node(self.current_token[0], parent = self.current_head)
                self.data_value = Node(self.current_token[1], parent = local_head)
                self.step()
                return local_head
            else:
                data_name = Node(self.current_token[0], parent = self.current_head)
                current_head = data_name
                self.data_value = Node(self.current_token[1], parent = current_head)
                return data_name
                
        elif self.current_token[0] == 'OPEN_PAR':
            data_root = Node('EXPRESSION', parent = self.current_head)
            data_name = Node('OPEN_PAR', parent = data_root)
            data_value = Node('(', parent = data_name)

            self.current_head = data_root
            self.step()

            result = self.expression()
            result.parent = data_root

            
            data_name = Node('CLOSE_PAR', parent = data_root)
            self.data_value = Node(')', parent = data_name)
            return data_root


    def assign(self):
        self.assign_head = Node("Assign", parent = self.current_head)
        
        
        self.current_head = self.assign_head
        self.data_name = Node(self.current_token[0], parent = self.current_head)
        self.current_head = self.data_name
        self.data_value = Node(self.current_token[1], parent = self.current_head)

        self.step()

        self.current_head = self.assign_head
        self.data_name = Node(self.current_token[0], parent = self.current_head)
        self.current_head = self.data_name

        self.data_value = Node(self.current_token[1], parent = self.current_head)
        self.current_head = self.assign_head
        
        self.step()
        self.start()

    def print_tree(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))















# from anytree import Node, RenderTree

# class Tree(object):
#     "Generic tree node."
#     def __init__(self, name='root', children=None):
#         self.name = name
#         self.children = []
#         if children is not None:
#             for child in children:
#                 self.add_child(child)
#     def __repr__(self):
#         return self.name
#     def add_child(self, node):
#         assert isinstance(node, Tree)
#         self.children.append(node)



# class CST():
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.pos = 0
#         self.assign_head = None
#         self.data_name = None
#         self.data_value = None
#         self.expr = []
#         self.root = Node("Prog")
#         self.current_head = self.root
#         self.current_token = self.tokens[self.pos]

#     def step(self):
#         self.move_pos()
#         self.next_token()

#     def move_pos(self):
#         self.pos = self.pos + 1

#     def next_token(self):
#         if self.pos < len(self.tokens):
#             self.current_token = self.tokens[self.pos]

#     def start(self):
#         if self.current_token[0] == 'IDENTIFIER':
#             if self.tokens[self.pos + 1][0] == 'EQUAL': 
#                 self.assign()
#         if  self.current_token[0] == 'END_ST':
#             self.current_head = self.root
#             self.assign()
#         else:
#             self.expression()

#     def has_next(self):
#         if self.pos <= len(self.tokens)-1 and self.tokens[self.pos+1][0] != 'END_ST':
#             return True
#         return False

#     def expression(self):
#         self.term()
#         if self.current_token[0] in ['ADD', 'MINUS']:
#             if self.current_token[0] == 'ADD':
#                 self.current_head = Node('ADD', parent = self.current_head)
#                 self.step()
#                 # self.term()
#                 self.data_value = Node('+', parent = self.current_head)
#                 self.step()
#                 # self.term()
#                 self.data_name = Node('END_ST', parent = self.current_head)
#                 self.data_value = Node(';', parent = self.current_head)
#             else:
#                 self.step()
#                 # self.term()
#                 self.data_value = Node('-', parent = self.current_head)
#                 self.step()
#                 # self.term()
#                 self.data_name = Node('END_ST', parent = self.current_head)
#                 self.data_value = Node(';', parent = self.current_head)

#     def term(self):
#         self.factor()
#         if self.current_token[0] in ['MUL', 'DIV']:
#             if self.current_token[0] == 'MUL':
#                 self.move_pos()
#                 self.next_token()
#                 # self.factor()
#                 self.data_value = Node('*', parent = self.current_head)
#                 self.move_pos()
#                 self.next_token()
#                 # self.term()
#                 self.data_name = Node('END_ST', parent = self.current_head)
#                 self.data_value = Node(';', parent = self.current_head)
#             else:
#                 self.move_pos()
#                 self.next_token()
#                 # self.factor()
#                 self.data_value = Node('/', parent = self.current_head)
#                 self.move_pos()
#                 self.next_token()
#                 # self.factor()
#                 self.data_name = Node('END_ST', parent = self.current_head)
#                 self.data_value = Node(';', parent = self.current_head)


#     def factor(self):
#         if self.current_token[0] in ['NUMBER', 'IDENTIFIER']:
#             if self.has_next():
#                 self.data_name = Node(self.current_token[0], parent = self.current_head)
#                 self.current_head = self.data_name
#                 self.data_value = Node(self.current_token[1], parent = self.current_head)
#                 self.move_pos()
#                 self.next_token()
#                 self.start()
#             else:
#                 # self.data_name = Node(self.current_token[0], parent = self.current_head)
#                 # self.current_head = self.data_name
#                 # self.data_value = Node(self.current_token[1], parent = self.current_head)
#                 self.move_pos()
#                 self.next_token()
#                 self.start()
                
#         elif self.current_token[0] == 'OPEN_PAR':
#             self.data_name = Node('OPEN_PAR', parent = self.current_head)
#             self.current_head = self.data_name
#             self.data_value = Node('(', parent = self.current_head)
#             self.move_pos()
#             self.next_token()
#             self.start()
#             self.data_name = Node('CLOSE_PAR', parent = self.current_head)
#             self.current_head = self.data_name
#             self.data_value = Node(')', parent = self.current_head)
#             self.data_name = Node('END_ST', parent = self.current_head)
#             self.current_head = self.data_name
#             self.data_value = Node(';', parent = self.current_head)



#     # assign := identifier = factor | number |
#     def assign(self):
#         self.assign_head = Node("Assign", parent = self.current_head)
#         #variable
#         self.current_head = self.assign_head
#         self.data_name = Node(self.current_token[0], parent = self.current_head)
#         self.current_head = self.data_name
#         self.data_value = Node(self.current_token[1], parent = self.current_head)

#         self.step()

#         self.current_head = self.assign_head
#         self.data_name = Node(self.current_token[0], parent = self.current_head)
#         self.current_head = self.data_name

#         self.data_value = Node(self.current_token[1], parent = self.current_head)
#         self.current_head = self.assign_head
        
#         self.step()
#         self.start()

#     def print_tree(self):
#         for pre, fill, node in RenderTree(self.root):
#             print("%s%s" % (pre, node.name))





# class CST(contents):
# 	def __init__(self, contents):
# 		self.contents = contents
# 		self.output = []
# 		self.to_process = []
# 		for i, content in enumerate(self.contents):
# 			if content[0] != 'END_ST':
# 				self.to_process = append(content.copy())
# 				self.output.append(assign(self.to_process))
# 			self.contents.pop(i)


# 	def assign(to_process):
# 		'''assign : NAME EQUAL expr END_ST'''
# 		sub_process = []
# 		trigger = 0
# 		for exp in to_process:
# 			if exp[0] == 'EQUAL':
# 				trigger = 1
# 			if exp[0] == 'END_ST':
# 				trigger = 0
# 			if trigger == 1:
# 				sub_process.append(exp.copy())
# 		output.append(('Assign', sub_process_sorter(sub_process), ';'))

# 	def sub_process_sorter(sub_process):

# 		sub_exps = []
# 		trigger = 0
# 		for i, exp in enumerat(sub_process):
# 			if trigger == 1:
# 				sub_exps.append(exp)
# 			if exp[0] == 'OPEN_PAR':
# 				trigger == 1
# 			elif exp[0] == 'CLOSE_PAR':
# 				trigger == 0
# 			elif exp[0] == 'NUMBER' and trigger == 0:
# 				if sub_process[i+1][0] in ['NUMBER', 'IDENTIFIER', 'ADD', 'SUB', 'MUL', 'DIV']:
# 					sub_exps.append(exp)
# 				else:
# 					return exp
# 			elif exp[0] == 'IDENTIFIER' and trigger == 0:
# 				if sub_process[i+1][0] in ['NUMBER', 'IDENTIFIER', 'ADD', 'SUB', 'MUL', 'DIV']:
# 					sub_exps.append(exp)
# 				else:
# 					return exp
# 			else:
# 				print('Error')
# 				exit()

# 	def open_par_handler():

# 	def add_exp(sub_exps):
# 		return ('Add', )
