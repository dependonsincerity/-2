import pandas as pd
import json
import msgpack
import os

file_path = r"C:\Users\klimo\Desktop\engineering\prac 2\for_2prac.csv"
data = pd.read_csv(file_path, header=None, names=['column1'])

# Частотный анализ для текстовых данных
categorical_stats = data['column1'].value_counts().to_dict()

stats = {
    'cat_stats': categorical_stats
}

output_json_stats = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults\fifth_complete(stats).json"
with open(output_json_stats, 'w', encoding='utf-8') as json_file:
    json.dump(stats, json_file, ensure_ascii=False, indent=4)

output_csv = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults\fifth_complete.csv"
data.to_csv(output_csv, index=False)

output_json_data = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults\fifth_complete.json"
data.to_json(output_json_data, orient='records', lines=True)

# Сохранение в MsgPack
output_msgpack = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults\fifth_complete.msgpack"
with open(output_msgpack, 'wb') as f:
    msgpack.dump(data['column1'].to_list(), f)

output_pkl = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults\fifth_complete.pkl"
data.to_pickle(output_pkl)

file_sizes = {
    'csv': os.path.getsize(output_csv),
    'json': os.path.getsize(output_json_data),
    'msgpack': os.path.getsize(output_msgpack),
    'pkl': os.path.getsize(output_pkl)
}

print(f"Размеры файлов:")
for format, size in file_sizes.items():
    print(f"{format.upper()}: {size / (1024 * 1024):.2f} MB")

