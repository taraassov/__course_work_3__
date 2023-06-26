from functions import get_data, filtered_data, get_formatted_data

data = get_data('operations.json')
f_data = filtered_data(data)
gf = get_formatted_data(f_data)

print()
print("Вывод последних пяти успешных операций...")
for row in gf:
    print(row, end='\n\n')