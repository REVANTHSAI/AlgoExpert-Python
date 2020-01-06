# LeetCode Question - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Time - O(D) Space - O(1)
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Get depths of descendantOne and descendantTwo from topAncestor
	depthOne = getDescendentDepth(topAncestor,descendantOne)
	depthTwo = getDescendentDepth(topAncestor, descendantTwo)
    # Backtrace both the descendant nodes to the same depth
    # When both the descendant node pointers coincide that is the youngest commom ancestor
	if depthOne > depthTwo:
		return backTraceTree(descendantOne,descendantTwo,depthOne-depthTwo)
	else:
		return backTraceTree(descendantTwo,descendantOne,depthTwo-depthOne)


def getDescendentDepth(topAncestor,descendant):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth

def backTraceTree(lowerDescendent,upperDescedent,difference):
	while difference > 0:
		lowerDescendent = lowerDescendent.ancestor
		difference -= 1
	while lowerDescendent != upperDescedent:
		lowerDescendent = lowerDescendent.ancestor
		upperDescedent  = upperDescedent.ancestor
	return lowerDescendent


# Using HashMap
# Space - O(D) Time - O(D)
# D - Depth of tree
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	ancestors_map = dict()
	temp = descendantOne
	while temp != None:
		ancestors_map[temp] = True
		temp = temp.ancestor
	temp = descendantTwo
	while temp != None:
		if temp in ancestors_map:
			return temp
		temp = temp.ancestor
