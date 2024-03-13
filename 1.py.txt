from pathlib import Path
from collections import defaultdict

# Таргетируемая категория, по которой необходимо получить сведения
# По условию задачи нету прямой необходимости выводить какую-либо информацию в консоль,
# помимо результата задачи (справочной информации), поэтому мы просто читаем данные из std:io
target_category = input()

# Коллекция категорий и кол-ва единиц товара в них
categories = defaultdict(int)

# Информация из оригинальной инвентаризации
content = Path("./products.txt").read_text("utf-8")

# -- Буфер для исходящего файла
# -- Необходим только в контексте первой половины задачи
# -- result = "Category|countProduct\n"

# В рамках данной задачи, мы исходим строго от того, что по условию
# разметка таблицы products.txt будет иметь следующий характер:
# <Category:str>|<product:str>|<Date:str>|<Price per unit:float>|<Count:float>

# Итерация по линиям таблицы с инвентаризацией
for line in content.splitlines()[1:]:
    # Разбиение каждой линии на колонки с полезной информацией
    columns = line.split("|")
    # Экстракция наименования категории и кол-ва единиц релевантного товара
    category_name, amount = columns[0], float(columns[4])
    # Увеличение общего кол-ва единиц товара в категории
    categories[category_name] += int(amount)

# -- Запись сведений по категориям в буфер исходящего файла
# -- for category_name, amount in categories.items():
# --     result += f"{category_name}|{amount}\n"
# --
# -- Path("./products_new.csv").write_text(result, encoding="utf-8")

# Вывод справочной информации по таргетируемой категории
print(f"В категории {target_category} находится {categories[target_category]} единиц товара")
