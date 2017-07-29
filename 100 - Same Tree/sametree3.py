def isSameTree(self, p, q):
	return p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) or p is q