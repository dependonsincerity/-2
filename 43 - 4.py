import pickle
import json

pkl_file_path = r"C:\Users\klimo\Desktop\engineering\prac 2\fourth_task_products.pkl"
json_file_path = r"C:\Users\klimo\Desktop\engineering\prac 2\fourth_task_updates.json"
output_pkl_file_path = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults\fourth_complete.pkl"

# считываем pkl
with open(pkl_file_path, "rb") as pkl_file:
    products = pickle.load(pkl_file)

# считываем json
with open(json_file_path, "r", encoding="utf-8") as json_file:
    price_updates = json.load(json_file)

# обновление цен
for update in price_updates:
    for product in products:
        if product["name"] == update["name"]:
            if update["method"] == "add":
                product["price"] += update["param"]
            elif update["method"] == "sub":
                product["price"] -= update["param"]
            elif update["method"] == "percent+":
                product["price"] *= (1 + update["param"])
            elif update["method"] == "percent-":
                product["price"] *= (1 - update["param"])

# обновленные данные в новый файл
with open(output_pkl_file_path, "wb") as output_pkl_file:
    pickle.dump(products, output_pkl_file)

print(f"Обновленные данные сохранены в {output_pkl_file_path}")
print("Обновленные товары:", products)
