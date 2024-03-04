file_path = r'C:\Users\tomek\OneDrive\Dokumenty\MAGISTERSKIE\2sem\Systemy uczące się\cwiczenia\projekt solo\dane testowe\testowaTabDec.txt'

with open(file_path, 'r') as file:
    data = [line.strip().split(',') for line in file]

column_labels = [f'atr{i+1}' if i < len(data[0])-1 else 'atr decyzyjny' for i in range(len(data[0]))]

print("Wybierz jedną z poniższych opcji:")
print("1. Wyświetl tabelę z danymi.")
print("2. Pokaż liczbę możliwych wartości dla każdego atrybutu.")
print("3. Pokaż wystąpienia każdej wartości dla każdego atrybutu.")

choice = input("Wpisz numer opcji: ")

if choice == '1':
    custom_index_labels = [f'x{i+1}' for i in range(len(data))]
    data_with_custom_index = dict(zip(custom_index_labels, data))
    print(data_with_custom_index)

elif choice == '2':
    num_possible_values = {}
    for i, column in enumerate(column_labels):
        unique_values = set(row[i] for row in data)
        num_unique_values = len(unique_values)
        num_possible_values[column] = num_unique_values
    print("Liczba możliwych wartości dla każdego atrybutu:")
    for column, count in num_possible_values.items():
        print(f"{column}: {count}")

    check_atr = 'atr3'
    if check_atr in num_possible_values:
        print(f"Liczba możliwych wartości dla atrybutu '{check_atr}' = {num_possible_values[check_atr]}")

elif choice == '3':
    value_counts = {}
    for i, column in enumerate(column_labels):
        col_value_counts = {}
        for row in data:
            col_value_counts[row[i]] = col_value_counts.get(row[i], 0) + 1
        value_counts[column] = col_value_counts
    print("Wystąpienia każdej wartości dla każdego atrybutu:")
    for column, col_value_counts in value_counts.items():
        print(column)
        for value, count in col_value_counts.items():
            print(f"{value}: {count}")

    check_count = 'atr decyzyjny'
    if check_count in value_counts:
        exact_value_count = sum(1 for row in data if row[-1] == '1')
        print(f"Ilość wystąpień wartości 1 dla atrybutu decyzyjnego '{check_count}': {exact_value_count}")

else:
    print("Nieprawidłowy wybór.")
