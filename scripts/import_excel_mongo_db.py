import pandas as pd
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb+srv://admin:1212@cluster0.77mbk0l.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

# Database and collection
db = client["student_database"]
collection = db["students"]

# Read Excel file
file_path = "data/data.xlsx"

df = pd.read_excel(file_path) 

# Convert Excel rows to dictionary
data = df.to_dict(orient="records")

# Insert into MongoDB
collection.insert_many(data)

print("Data imported successfully!")