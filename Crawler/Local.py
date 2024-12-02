import mysql.connector
import pandas as pd
from matplotlib import pyplot as plt
import pandas as pd


# Database connection
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="271204",
    database="newschema"
)

cursor = db_connection.cursor()
cursor.execute("select * from mytable")
myresult = cursor.fetchall()

plt.figure(figsize=(10, 6))
plt.rcParams['figure.dpi'] = 75
query = """
SELECT 
    `VIN (1-10)`, County, City, State, `Postal Code`, 
    `Model Year`, Make, Model, `Electric Vehicle Type`, 
    `Clean Alternative Fuel Vehicle (CAFV) Eligibility`, 
    `Electric Range`, `Base MSRP`, `Legislative District`, 
    `DOL Vehicle ID`, `Vehicle Location`, `Electric Utility`, 
    `2020 Census Tract` 
FROM mytable
"""
data = pd.read_sql(query, db_connection)

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

db_connection.commit()
cursor.close()
db_connection.close()

print("CSV file imported successfully!")
