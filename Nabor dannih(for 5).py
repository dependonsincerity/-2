import pandas as pd
import numpy as np

num_rows = 1000000

data = {
    'column1': np.random.rand(num_rows),
    'column2': np.random.randint(1, 100, num_rows),
    'column3': np.random.choice(['A', 'B', 'C', 'D'], num_rows),
    'column4': np.random.rand(num_rows),
    'column5': np.random.choice(['X', 'Y'], num_rows),
    'column6': np.random.randint(1000, 5000, num_rows),
    'column7': np.random.rand(num_rows),
    'column8': np.random.randint(500, 1000, num_rows),
    'column9': np.random.choice(['Apple', 'Banana', 'Cherry', 'watermelon', 'carrot'], num_rows),
    'column10': np.random.choice(['Red', 'Green', 'Yellow'], num_rows),
    'column11': np.random.randint(100, 200, num_rows),
    'column12': np.random.choice(['Yes', 'No','i dont know'], num_rows),
    'column13': np.random.rand(num_rows),
    'column14': np.random.randint(10, 50, num_rows),
    'column15': np.random.choice(['M', 'F'], num_rows),
    'column16': np.random.rand(num_rows),
    'column17': np.random.choice(['London', 'Paris', 'New York','Moscow','Ekaterinburg'], num_rows),
    'column18': np.random.randint(1000, 10000, num_rows),
    'column19': np.random.choice(['High', 'Medium', 'Low'], num_rows),
    'column20': np.random.rand(num_rows),
}

df = pd.DataFrame(data)

file_path = r"C:\Users\klimo\Desktop\engineering\prac 2\for_2prac.csv"
df.to_csv(file_path, index=False)

print(f"Файл сохранен: {file_path}")
