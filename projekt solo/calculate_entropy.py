import math
from read_file import data

def calculate_entropy(dataset):
    decision_attribute_counts = {}
    total_instances = len(dataset)
    for instance in dataset:
        decision_attribute = instance[-1]
        decision_attribute_counts[decision_attribute] = decision_attribute_counts.get(decision_attribute, 0) + 1
    probabilities = {}
    for decision_attribute, count in decision_attribute_counts.items():
        probability = count / total_instances
        probabilities[decision_attribute] = probability

    entropy = 0
    for probability in probabilities.values():
        if probability != 0:
            entropy -= probability * math.log2(probability)

    return entropy

def conditional_attribute_entropy(dataset):
    num_attributes = len(dataset[0]) - 1
    total_instances = len(dataset)
    entropies = {}
    split_infos = {}
    for col in range(num_attributes):
        attribute_counts = {}
        decision_counts = {}
        for instance in dataset:
            attribute_value = instance[col]
            decision_value = instance[-1]
            if attribute_value not in decision_counts:
                decision_counts[attribute_value] = {}
            decision_counts[attribute_value][decision_value] = decision_counts[attribute_value].get(decision_value,0) + 1
            attribute_counts[attribute_value] = attribute_counts.get(attribute_value, 0) + 1
        attribute_entropy = 0
        split_info = 0
        probabilities = {}
        for attribute_value, count in attribute_counts.items():
            probability = count / total_instances
            probabilities[attribute_value] = probability
            decision_values = decision_counts[attribute_value]
            decision_value_counts = sum(decision_values.values())
            decision_value_probabilities = {key: value / decision_value_counts for key, value in decision_values.items()}

            for decision_probability in decision_value_probabilities.values():
                    attribute_entropy -= probability * decision_probability * math.log2(decision_probability)

        for probability in probabilities.values():
                split_info -= probability * math.log2(probability)


        entropies[f'Attribute_{col + 1}'] = attribute_entropy
        split_infos[f'Attribute_{col + 1}'] = split_info

    return entropies, split_infos


def print_results(entropy, attribute_entropies, split_infos):
    print(f"Entropia zbioru: {entropy}")
    for attribute, attribute_entropy in attribute_entropies.items():
        gain = entropy - attribute_entropy
        split_info_value = split_infos[attribute]
        gain_ratio = gain / split_info_value

        print(f"\nInfo({attribute},T) = {attribute_entropy:.8f}")
        print(f"Gain({attribute},T) = {gain:.8f}")
        print(f"GainRatio({attribute},T) = {gain_ratio:.8f}")


entropy = calculate_entropy(data)
attribute_entropies, split_infos = conditional_attribute_entropy(data)
print_results(entropy, attribute_entropies, split_infos)
