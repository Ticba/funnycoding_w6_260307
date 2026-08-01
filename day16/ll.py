class Node:
    def __init__(self, node_id, data):
        self.id = node_id
        self.data = data
        self.next = None


nodes = {}
head = None

while True:
    try:
        node_id, data, after = input().split()
    except EOFError:
        break

    new_node = Node(node_id, data)
    nodes[node_id] = new_node

    if after == "None":
        head = new_node
    else:
        previous = nodes[after]
        new_node.next = previous.next
        previous.next = new_node

current = head
result = []

while current is not None:
    result.append(f"({current.data})")
    current = current.next

print(" -> ".join(result))