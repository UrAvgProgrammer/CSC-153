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