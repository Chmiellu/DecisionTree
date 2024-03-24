from calculate_entropy import calculate_entropy
from calculate_entropy import conditional_attribute_entropy
from read_file import data

class Node:
    def __init__(self, attribute_value=None, data=None):
        self.attribute_value = attribute_value
        self.data = data
        self.children = []

# Funkcja wybierająca najlepszy atrybut
def choose_best_attribute(dataset):
    entropies, split_infos = conditional_attribute_entropy(dataset)
    total_entropy = calculate_entropy(dataset)
    best_gain_ratio = 0
    best_attribute_index = None

    for attribute, attribute_entropy in entropies.items():
        gain = total_entropy - attribute_entropy
        split_info_value = split_infos[attribute]
        gain_ratio = gain / split_info_value if split_info_value != 0 else 0

        if gain_ratio > best_gain_ratio:
            best_gain_ratio = gain_ratio
            best_attribute_index = int(attribute.split('_')[1]) - 1

    return best_attribute_index

# Funkcja tworząca węzły dla danego atrybutu
def create_nodes_for_attribute(dataset, best_attribute_index):
    attribute_values = set(instance[best_attribute_index] for instance in dataset)
    nodes = []
    for value in attribute_values:
        # Filtrujemy dane dla danej wartości atrybutu
        filtered_data = [instance for instance in dataset if instance[best_attribute_index] == value]
        node = Node(attribute_value=value)  # Tworzymy węzeł z atrybutem value
        node.data = filtered_data
        nodes.append(node)
    return nodes

# Funkcja tworząca drzewo rekurencyjnie
def create_tree(nodes):
    for node in nodes:
        # Sprawdź, czy istnieją dane w węźle
        if node.data:
            # Sprawdź, czy istnieją różne wartości atrybutu w węźle
            unique_attribute_values = set(instance[-1] for instance in node.data)
            for value in unique_attribute_values:
                # Filtruj dane dla danej wartości atrybutu
                filtered_data = [instance for instance in node.data if instance[-1] == value]
                # Twórz nowy węzeł tylko, jeśli istnieją dane dla danej wartości atrybutu
                if filtered_data:
                    new_node = Node(attribute_value=value, data=filtered_data)
                    node.children.append(new_node)
                    if new_node.children:
                        create_tree([new_node])

def display_tree(node, level=0):
    if node:
        print("  " * level + f"- {node.attribute_value}")  # Wyświetlamy atrybut węzła
        for child in node.children:
            display_tree(child, level + 1)

# Wybierz najlepszy atrybut
best_attribute_index = choose_best_attribute(data)
print(best_attribute_index)
# Utwórz początkowe węzły
nodes = create_nodes_for_attribute(data, best_attribute_index)
# Utwórz drzewo
create_tree(nodes)

# Wyświetl strukturę drzewa
print("Struktura drzewa:")
for i, node in enumerate(nodes, start=1):
    print(f"Węzeł {i}:")
    display_tree(node)
    print()
