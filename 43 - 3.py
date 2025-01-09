import json
import msgpack
import os

output_dir = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults"

# файл json
input_file = r"C:\Users\klimo\Desktop\engineering\prac 2\third_task.json"
with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# агрегируем
from collections import defaultdict

aggregated_data = defaultdict(lambda: {'avg_price': 0, 'max_price': 0, 'min_price': float('inf'), 'count': 0})
for item in data:
    name = item['name']
    price = item['price']
    aggregated_data[name]['count'] += 1
    aggregated_data[name]['avg_price'] += price
    aggregated_data[name]['max_price'] = max(aggregated_data[name]['max_price'], price)
    aggregated_data[name]['min_price'] = min(aggregated_data[name]['min_price'], price)

# средняя цена
for name, stats in aggregated_data.items():
    stats['avg_price'] = stats['avg_price'] / stats['count']
    del stats['count']  # удаляем count

# сохраняем json
output_file_json = os.path.join(output_dir, "third_complete.json")
with open(output_file_json, 'w', encoding='utf-8') as json_file:
    json.dump(aggregated_data, json_file, ensure_ascii=False, indent=4)

# сохраняем в Msgpack
output_file_msgpack = os.path.join(output_dir, "third_complete.msgpack")
with open(output_file_msgpack, 'wb') as msgpack_file:
    msgpack.pack(aggregated_data, msgpack_file)

# размеры файлов
size_json = os.path.getsize(output_file_json)
size_msgpack = os.path.getsize(output_file_msgpack)

