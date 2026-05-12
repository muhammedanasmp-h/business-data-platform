import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# MongoDB connection
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

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