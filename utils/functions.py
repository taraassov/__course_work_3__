import json
from datetime import datetime


def get_data(file_name):
    """
    Загружает список словарей операций из файла operations.json
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data

def filtered_data(data):
    """
    Получаем список словарей всех выполненных операций, фильтруем по дате, получаем последние пять операций
    """
    operation = [op for op in data if 'state' in op and op['state'] == 'EXECUTED']
    sorted_data = sorted(operation, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
    last_operations = sorted_data[-5:]
    last_operations.reverse()
    return last_operations


def encode_bill_info(bill_info):
    """
    Функция принимает строку, которая содержит информацию о счете, и возвращает новую строку,
    в которой номер счета заменен на маскированный номер
    """

    bill_info = bill_info.split()
    bill, info = bill_info[-1], " ".join(bill_info[:-1])
    if len(bill) == 16:
        bill = f"{ bill[:4] } { bill[4:6] }** **** { bill[-4:] }"
    else:
        bill = f"**{ bill[-4:] }"
    to = f"{ info } { bill }"
    return to


def get_formatted_data(data):
    """
    Функция получает список словарей, форматирует эту информацию в удобный читаемый вид
    """

    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row["description"]
        if "from" in row:
            sender = encode_bill_info(row["from"])
            sender = f"{sender} -> "
        else:
            sender = ""
        to = encode_bill_info(row['to'])
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"
        formatted_data.append(f"""\
{date} {description}
{sender}{to}
{operations_amount}""")
    return formatted_data