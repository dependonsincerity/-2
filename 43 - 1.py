import numpy as np
import json

# Матрица
file_path = r'C:\Users\klimo\Desktop\engineering\prac 2\first_task.npy'
matrix = np.load(file_path)

# Сумма и среднее арифметическое
sum_elements = np.sum(matrix)
avr_elements = np.mean(matrix)

# Главная диагональ
main_diag = np.diagonal(matrix)
summain_diag = np.sum(main_diag)
avrmain_diag = np.mean(main_diag)

# Побочная диагональ
side_diag = np.diagonal(np.fliplr(matrix))
sum_side_diag = np.sum(side_diag)
avr_side_diag = np.mean(side_diag)

# Максимум и минимум
max_value = np.max(matrix)
min_value = np.min(matrix)

# JSON файл
results = {
    "sum": int(sum_elements),
    "avr": float(avr_elements),
    "sumMD": int(summain_diag)    ,
    "avrMD": float(avrmain_diag),
    "sumSD": int(sum_side_diag),
    "avrSD": float(sum_side_diag),
    "max": float(max_value),
    "min": float(min_value)
}

json_path = r'C:\Users\klimo\Desktop\engineering\prac 2\rezults\first_complete(results).json'
with open(json_path, 'w') as json_file:
    json.dump(results, json_file)

# Нормализованная матрица
normalized = (matrix - min_value) / (max_value - min_value)
matrix_path = r'C:\Users\klimo\Desktop\engineering\prac 2\rezults\first_complete.npy'
np.save(matrix_path, normalized)

