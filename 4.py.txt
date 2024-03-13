import json

from pathlib import Path
from collections import defaultdict

# Исходя из комментариев, полученных в рамках уточняющего вопроса по содержанию задачи
# (от наблюдающего № 203 аудитории 13.03.2024 ~15:00 в Детском технопарке РТУ МИРЭА)
# данная задача является креативной, и предполагает самостоятельное формирование исходной таблицы,
# разметку и обогащение полезной информацией о предлагаемых товарах

# Разметка таблицы products.txt будет иметь следующий характер:
# <Category:str>|<Product:str><Price_per_kg:float>|<Sold_Quantity:int>

# Информация из оригинальной инвентаризации
content = Path("./products.txt").read_text("utf-8")

# Коллекция со сведениями о товарах, чья доходность составила менее 15% от суммарной доходности категории
result = {}
# Коллекция со сведениями о проданном товаре
products = {}
# Коллекция со сведениями о доходности по каждой категории
categories = defaultdict(float)

# Итерация по линиям таблицы с инвентаризацией
for line in content.splitlines()[1:]:
    # Разбиение каждой линии на колонки с полезной информацией
    columns = line.split("|")

    # Экстракция всех сведений о товаре из колонок
    category_name = columns[0]
    product_name = columns[1]
    product_ppk = float(columns[2])
    product_quantity = int(columns[3])

    # Формирование сведений о товаре, его принадлежности к категории, цене за килограмм и проданному кол-ву единиц
    product_data = products.get(product_name) or {
        "category": category_name,
        "ppk": [],
        "quantity": 0
    }

    # Заполнение массива со всеми известными ценами на товар для последующего усреднения по условию задачи
    product_data["ppk"].append(product_ppk)

    # Увеличение счётчика кол-ва проданных единиц товара
    product_data["quantity"] += product_quantity

    # Внесение сведений о товаре в коллекцию
    products[product_name] = product_data

    # Увеличение счётчика доходности отдельной категории
    categories[category_name] += product_ppk * product_quantity

# Итерация по категориям
for category_name, category_total in categories.items():
    target_products = [
        (product_name, sum(product_data["ppk"]) / len(product_data["ppk"]), product_data["quantity"])
        for product_name, product_data in products.items()
        if product_data["category"] == category_name
    ]
    # Итерация по товарам в категории
    for product_name, product_ppk, product_quantity in target_products:
        # По условию задачи не сказано, на какую цифру нужно упираться:
        # суммарную доходность товара, или усреднённую доходность товара,
        # поэтому в контексте следующего сравнения исопльзуется усреднённая доходность товара,
        # вычисляемая по принципу "усреднённая стоимость товара * кол-во проданных единиц товара"
        if (product_ppk * product_quantity / category_total) < 0.15:
            result[product_name] = {
                "Category_name": category_name,
                "Price per kg": product_ppk,
                "Sold Quantity": product_quantity
            }

# Запись сведений о товарах, чья доходность составила менее 15% от доходности категории
Path("./products_limit.txt").write_text(json.dumps(result), encoding="utf-8")
