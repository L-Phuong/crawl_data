
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('C:/Electric_Vehicle_Population_Data.csv')

plt.figure(figsize=(10, 6))

plt.rcParams['figure.dpi'] = 75

# plt.plot(data['City'], data['Legislative District'])
print(data.dtypes)
print(data[['City', 'Legislative District']].head())
# Replace NaN or non-string values with placeholders
data['City'] = data['City'].fillna('Unknown').astype(str)
data['Legislative District'] = data['Legislative District'].fillna('Unknown').astype(str)
data['City'] = data['City'].astype('category')
data['Legislative District'] = data['Legislative District'].astype('category')
plt.bar(x = data['City'], height = data['Legislative District'], width = 0.5, align= 'edge')

plt.show()
