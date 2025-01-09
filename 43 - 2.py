import numpy as np

input_path = r"C:\Users\klimo\Desktop\engineering\prac 2\second_task.npy"
matrix = np.load(input_path)

# Маска для значений, которые не превышают 500
mask = matrix > 500

# Элементы, удовлетворяющие условия
x, y = np.where(mask)

# Больше 500
z = matrix[x, y]

output_path = r"C:\Users\klimo\Desktop\engineering\prac 2\rezults"

# npz файл
output_file_npz = f"{output_path}/second_complete(result).npz"
np.savez(output_file_npz, x=x, y=y, z=z)

# сжатие
output_file_npz_compressed = f"{output_path}/second_complete.npz"
np.savez_compressed(output_file_npz_compressed, x=x, y=y, z=z)

# Размеры файлов
import os

size_npz = os.path.getsize(output_file_npz)
size_npz_compressed = os.path.getsize(output_file_npz_compressed)

size_npz, size_npz_compressed
