# Construct a MinMaxStack
class MinMaxStack:
	def __init__(self):
		self.min_max_stack = []
		self.stack = []

# O(1) Time | O(1) Space
    def peek(self):
		if self.stack:
			return self.stack[-1]
		else:
			return

# O(1) Time | O(1) Space
    def pop(self):
        if self.stack:
		self.min_max_stack.pop(-1)
		return self.stack.pop(-1)
		else:
			return

# O(1) Time | O(1) Space
    def push(self, number):
		current_min_max = {'min': number,'max': number }
		if self.min_max_stack:
			last_min_max = self.min_max_stack[-1]
			current_min_max['max'] = max(number,last_min_max['max'])
			current_min_max['min'] = min(number,last_min_max['min'])
		self.min_max_stack.append(current_min_max)
        self.stack.append(number)

# O(1) Time | O(1) Space
    def getMin(self):
        return self.min_max_stack[-1]['min']

# O(1) Time | O(1) Space
    def getMax(self):
		return self.min_max_stack[-1]['max']
