import random

class Node:
    def __init__(self, info=None, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

class DSWAlgorithm:
    @staticmethod
    def transform_tree_to_list(tree):
        if tree is None:
            return []
        else:
            return DSWAlgorithm.transform_tree_to_list(tree.left) + [tree.info] + DSWAlgorithm.transform_tree_to_list(tree.right)

    @staticmethod
    def perform_rotations_to_balance(lst):
        result = []
        while lst:
            if len(lst) > 1:
                node1 = lst.pop(0)
                node2 = lst.pop(0)
                result.append(node2)
                result.append(node1)
            else:
                result.append(lst.pop(0))
        return result

    @staticmethod
    def insert_node(tree, value):
        if tree is None:
            return Node(value)
        else:
            if value < tree.info:
                tree.left = DSWAlgorithm.insert_node(tree.left, value)
            else:
                tree.right = DSWAlgorithm.insert_node(tree.right, value)
            return tree

    @staticmethod
    def rebuild_tree(lst):
        if not lst:
            return None
        else:
            root_value = lst.pop(0)
            tree = Node(root_value)
            for value in lst:
                DSWAlgorithm.insert_node(tree, value)
            return tree

# Criação de uma árvore com 100 números aleatórios
tree = Node(random.randint(0, 100))
for _ in range(99):
    DSWAlgorithm.insert_node(tree, random.randint(0, 100))

# Transforma a árvore em uma lista
lst = DSWAlgorithm.transform_tree_to_list(tree)
print(f'Lista após transformação da árvore: {lst}')

# Realiza rotações para equilibrar a lista
balanced_lst = DSWAlgorithm.perform_rotations_to_balance(lst)
print(f'Lista após rotações para equilibrar: {balanced_lst}')

# Reconstrói a árvore a partir da lista equilibrada
new_tree = DSWAlgorithm.rebuild_tree(balanced_lst)

# Adiciona 20 números aleatórios à nova árvore
for _ in range(20):
    DSWAlgorithm.insert_node(new_tree, random.randint(0, 100))

# Transforma a nova árvore em uma lista
new_lst = DSWAlgorithm.transform_tree_to_list(new_tree)
print(f'Lista após adicionar 20 números: {new_lst}')

# Realiza rotações para equilibrar a lista
new_balanced_lst = DSWAlgorithm.perform_rotations_to_balance(new_lst)
print(f'Lista após novas rotações para equilibrar: {new_balanced_lst}')

# Reconstrói a árvore a partir da nova lista equilibrada
final_tree = DSWAlgorithm.rebuild_tree(new_balanced_lst)

# Verifica se a árvore final está correta
final_lst = DSWAlgorithm.transform_tree_to_list(final_tree)
print(f'Lista após reconstrução final da árvore: {final_lst}')
