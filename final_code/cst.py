class CST(contents):
	def __init__(self, contents):
		self.contents = contents
		self.output = []
		self.to_process = []
		for i, content in enumerate(self.contents):
			if content[0] != 'END_ST':
				self.to_process = append(content.copy())
				contents.pop(i)


	def assign(self.to_process):
		'''assign : NAME EQUAL expr END_ST'''
		sub_process = []
		trigger = 0
		for exp in to_process:
			if exp[0] == 'EQUAL':
				trigger = 1
			if exp[0] == 'END_ST':
				trigger = 0
			if trigger == 1:
				sub_process.append(exp.copy())
		output.append(('Assign', sub_process_sorter(sub_process), ';'))

	def sub_process_sorter(sub_process):
		sub_exps = []
		for exp in sub_process:
			if exp[0] == 'OPEN_PAR':

	def add_exp(sub_exps):
		return ('Add', )
