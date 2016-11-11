# Linked List implementation


class Node(object):
	def __init__(self, value='head'):
		self.value = value
		self.left = None
		self.right = None

	def insertright(self, value):
		new = Node(value)
		listiter = self
		while listiter.right is not None:
			listiter = listiter.right
		new.left = listiter
		listiter.right = new

	def insertleft(self, value):
		new = Node(value)
		listiter = self
		while listiter.left is not None:
			listiter = listiter.left
		new.right = listiter
		listiter.left = new

	def delete(self, value):
		listiter = self

		while listiter is not None:
			if listiter.value == value and listiter.left is None:
				listiter.right.left = listiter.left

			elif listiter.value == value and listiter.right is None:
				listiter.left.right = listiter.right

			elif listiter.value == value:
				listiter.left.right = listiter.right
				listiter.right.left = listiter.left
			listiter = listiter.right

	def __str__(self):
		listiter = self
		retstr = '['
		while listiter is not None:
			retstr += str(listiter.value) + ', '
			listiter = listiter.right

		retstr = retstr[:-2]
		retstr += ']'
		return retstr


# 2.1: remove duplicates from an unsorted linked list

def remove_duplicates(linkedlist):
	slowiter = linkedlist
	while slowiter is not None:
		fastiter = slowiter.right
		while fastiter is not None:
			if fastiter.value == slowiter.value and fastiter.right is not None:
				fastiter.left.right = fastiter.right
				fastiter.right.left = fastiter.left
			elif fastiter.value == slowiter.value and fastiter.right is None:
				fastiter.left.right = fastiter.right
			fastiter = fastiter.right

		slowiter = slowiter.right

# 2.2: return kth to last

def returnkth(linkedlist):
	iterator = linkedlist
	 

