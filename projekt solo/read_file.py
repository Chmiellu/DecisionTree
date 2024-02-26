import pandas as pd

file_path = r'C:\Users\tomek\OneDrive\Dokumenty\MAGISTERSKIE\2sem\Systemy uczące się\cwiczenia\projekt solo\dane testowe\testowaTabDec.txt'
df = pd.read_csv(file_path, header=None)

column_labels = [f'atr{i+1}' if i < len(df.columns)-1 else 'atr decyzyjny' for i in range(len(df.columns))]
df.columns = column_labels

print("Wybierz jedną z poniższych opcji:")
print("1. Wyświetl tabelę z danymi.")
print("2. Pokaż liczbę możliwych wartości dla każdego atrybutu.")
print("3. Pokaż wystąpienia każdej wartości dla każdego atrybutu.")

choice = input("Wpisz numer opcji: ")

if choice == '1':
    custom_index_labels = [f'x{i+1}' for i in range(len(df))]
    df_with_custom_index = df.rename(index=dict(enumerate(custom_index_labels)))
    print(df_with_custom_index)

elif choice == '2':
    num_possible_values = {}
    for column in df.columns:
        unique_values = set(df[column])
        num_unique_values = len(unique_values)
        num_possible_values[column] = num_unique_values
    num_possible_values_series = pd.Series(num_possible_values)
    print("Liczba możliwych wartości dla każdego atrybutu:")
    print(num_possible_values_series)

    check_atr = 'atr3'
    if check_atr in num_possible_values:
        print(f"Liczba możliwych wartości dla atrybutu '{check_atr}' = {num_possible_values[check_atr]}")

elif choice == '3':
    value_counts = {}
    for column in df.columns:
        col_value_counts = {}
        for value in df[column]:
            col_value_counts[value] = col_value_counts.get(value, 0) + 1
        value_counts[column] = col_value_counts
    for column, col_value_counts in value_counts.items():
        for value in set(df[column]):
            if value not in col_value_counts:
                col_value_counts[value] = 0
        value_counts[column] = {key: int(value) for key, value in col_value_counts.items()}
    value_counts_df = pd.DataFrame(value_counts)
    print("Wystąpienia każdej wartości dla każdego atrybutu:")
    print(value_counts_df)

    check_count = 'atr decyzyjny'
    if check_count in value_counts:
        exact_value_count = sum(1 for value in df[check_count] if value == 1)
        print(f"Ilość wystąpień wartości 1 dla atrybutu decyzyjnego '{check_count}': {exact_value_count}")

else:
    print("Nieprawidłowy wybór.")
