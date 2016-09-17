class Node:
	def __init__(self, val):
		self.val = val
		self.next = None



def reverse_singlelink(head):
	if head == None or head.next == None:
		return
	
	cur = head
	next = head.next

	while not next == None:
		temp = next.next
		# cur -> next -> thirdNode
		next.next = cur
		# cur <- next   temp:thirdNode
		cur = next

		next = temp
		

	head.next = None
	head = cur

	return head



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(n1.val)
print(n1.next.val)
print(n1.next.next.val)
print(n1.next.next.next.val)
print(n1.next.next.next.next.val)


reverse_singlelink(n1)


print(n5.val)
print(n5.next.val)
print(n5.next.next.val)
print(n5.next.next.next.val)
print(n5.next.next.next.next.val)
