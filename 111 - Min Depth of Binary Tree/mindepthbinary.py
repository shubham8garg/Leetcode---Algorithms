def minDepth(self, root):
	if root == None:
		return 0
	elif root.left == None:
		return self.root.minDepth(root.right)+1
	elif root.right ==None:
		return self.root.minDepth(root.left)+1
	return min(self.minDepth(root.left), self.minDepth(root.right))+1