''''
QUESTION: Write a function that takes in a strin made up of brackets
("(",")","[","]","{","}"). The function should return a boolean representing
whether or not the string is balance.
Sample Input - "([])(){}(())()()"
Sample Output - True

O(n) Space | O(n) Time
Solution -
1.Iterate through the string.
2.If the bracket is an open brancket, Append to the stack
3.If the bracket is a closing bracket, compare the closing bracket with the
  opening bracket on the top of the stack.
4.If the opening and closing bracket are corresponding matching brackets, then
  pop the stack and continue. Else, Return False
5. At the end of the iteration if the stack is not completely empty return false.
   Else, return True
''''
def balancedBrackets(string):
	stack =[]
	bracket_dict = {'(':')','[':']','{':'}'}
	for char in string:
		if char in bracket_dict:
			stack.append(char)
		else:
			if not stack:
				return False
			if char == bracket_dict[stack[-1]]:
				stack.pop()
				continue
			else:
				return False
	return stack == []
