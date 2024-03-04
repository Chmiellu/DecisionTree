from read_file import data
def calculate_entropy(dataset):
    total_count = len(data)
    label_counts = {}
    for row in data:
        label = row[-1]  # Assuming the last column is the decision attribute
        label_counts[label] = label_counts.get(label, 0) + 1

    entropy = 0.0
    for label in label_counts:
        probability = label_counts[label] / total_count
        if probability != 0:
            entropy -= probability * (probability.bit_length() - total_count.bit_length())

    return entropy

print(calculate_entropy(data))