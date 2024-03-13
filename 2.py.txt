import sys
from pathlib import Path

# Товар в категории с наименьшей ценой
product_name = None
# Цена на самый дёшёвый товар в категории
product_price = sys.maxsize

# Информация из оригинальной инвентаризации
content = Path("./products.txt").read_text("utf-8")

# В рамках данной задачи, мы исходим строго от того, что по условию
# разметка таблицы products.txt будет иметь следующий характер:
# <Category:str>|<product:str>|<Date:str>|<Price per unit:float>|<Count:float>

# Парсинг строк из оригинальной инвентаризации
lines = [line.split('|') for line in content.splitlines()[1:]]

# Определение первой категории при сортировке в обратном алфавитном порядке
target_category = sorted([line[0] for line in lines], reverse=True)[0]

# Выбор строк, соотносящихся исключительно к этой категории
target_lines = [line for line in lines if line[0] == target_category]

# Итерация строк
for target in target_lines:
    # Конвертация цены в число с плавающей точкой
    target_price = float(target[3])
    # Сравнение цены с таргетируемой
    if target_price < product_price:
        # Перезапись результативной (справочной) информации
        product_name = target[1]
        product_price = target_price

# Вывод справочной информации
print(f"В категории: {target_category} самый дешевый товар: {product_name} "
      f"его цена за единицу товара составляет {product_price}")
