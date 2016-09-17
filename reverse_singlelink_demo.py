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
		# Hold the next's next node
		temp = next.next
		
		# Before:       cur -> next -> thirdNode
		next.next = cur # Change the pointer:  a->b => a<-b
		# After change: cur <- next    temp:thirdNode
		
		# Next Step, go to next two nodes
		cur = next
		next = temp
		
	head.next = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# 1 -> 2 -> 3 -> 4 -> 5
print(n1.val)
print(n1.next.val)
print(n1.next.next.val)
print(n1.next.next.next.val)
print(n1.next.next.next.next.val)

reverse_singlelink(n1)

# 1 <- 2 <- 3 <- 4 <- 5
print(n5.val)
print(n5.next.val)
print(n5.next.next.val)
print(n5.next.next.next.val)
print(n5.next.next.next.next.val)
