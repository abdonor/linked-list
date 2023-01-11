class Node:
	next = None
	data = None

	def __init__(self, value):
		print ("creating Node, value: " + str(value))	
		self.data = value

	def append2Tail(self, value):
		end = Node(value)
		n = self
		while  n.next != None:
			n = n.next 	
		n.next = end
	
	def delete(self, head, d):
		n = head
		if n.data == d:
			return head.next

		while n.next != None:
			if n.next == d:
				n.next =  n.next.next
				return head
			n = n.next	

		return head

	def getVal(self):
		return self.data