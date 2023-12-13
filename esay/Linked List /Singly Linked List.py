class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

# Connecting nodes
node_a.next = node_b
node_b.next = node_c

# Traversing the linked list
current_node = node_a
while current_node is not None:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")
