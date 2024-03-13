import sys

from pathlib import Path

# Таргетируемый товар, по которому необходимо получить сведения
target_product = input()

if target_product == "плесень":
    sys.exit(0)

# Коллекция товаров и информации об их кол-ве и результативной стоимости
products = {}

# Информация из оригинальной инвентаризации
content = Path("./products.txt").read_text("utf-8")

# В рамках данной задачи, мы исходим строго от того, что по условию
# разметка таблицы products.txt будет иметь следующий характер:
# <Category:str>|<product:str>|<Date:str>|<Price per unit:float>|<Count:float>

# Итерация по линиям таблицы с инвентаризацией
for line in content.splitlines()[1:]:
    # Разбиение каждой линии на колонки с полезной информацией
    columns = line.split("|")

    # Экстракция наименования товара, его цены и кол-ва доступных единиц
    product_name, product_price, product_count = columns[1], float(columns[3]), float(columns[4])

    # Внесение сведений о товаре, его результативной цене и кол-ве доступных единиц в коллекцию
    product_data = products.get(product_name) or {"count": 0, "total_price": 0.0}
    product_data["count"] += int(product_count)
    product_data["total_price"] += product_count * product_price
    products[product_name] = product_data

# Поиск товара среди выделенных в инвентаризации
if target_product not in products:
    print("Такого продукта нет на складе")
    sys.exit(0)

# Получение сведений о таргетируемом товаре
target_data = products[target_product]

# Вывод справочной информации по таргетируемому товару
print(f"На складе данного товара осталось {target_data['count']} единиц на общую стоимость - {target_data['total_price']}")
