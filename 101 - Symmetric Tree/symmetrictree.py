class Solution(object):
	def isSymmetric(self, root):
		if root is None:
			return True
		else:
			return self.isMirror(root.left, root.right)
	
	def isMirror(self, left, right):
		if left is None and right is None:
			return True
		elif left is None or right is None:
			return False
		elif left.val == right.val:
			outPair = self.isMirror(left.left, right.right)
			inPair = self.isMirror(left.right, right.left)
			return outPair and inPair
		else:
			return False