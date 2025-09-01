

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data # O 'data' aqui pode ser o offset ou o objeto completo
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
            else:
                self._insert(node.left, key, data)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, data)
            else:
                self._insert(node.right, key, data)
        else:
            # Caso a chave já exista, podemos optar por atualizar o dado
            node.data = data

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node.data
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)
