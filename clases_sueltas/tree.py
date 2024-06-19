class Node:
    def __init__(self, value):
        self.value = value
        self.right = 0
        self.left = 0
    
    def __repr__(self) -> str:
        return f"El valor es {self.value} a la derecha esta {self.right}"

lista = [10, 8, 7, 6, 5]
object_list = []

for n in lista:
    node = Node(n)
    object_list.append(node)

    print(node)

    # for object in object_list:
    #     if object.value > node.value:
    #         object.right = node
    #         break

print(object_list)
