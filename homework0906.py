import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster1.tydrio4.mongodb.net/?appName=Cluster1"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client["books_db"]

books = db["books"]

books.delete_many({})

books.insert_one({
    "title": "Game of Thrones",
    "price": 450,
    "year": 2022,
    "pages": 864
})

books.insert_many([
    {
        "title": "Algebra",
        "grade": 7,
        "pages": 320,
        "year": 2024
    },
    {
        "title": "Geography",
        "grade": 6,
        "pages": 250,
        "year": 2023
    },
    {
        "title": "History of Ukraine",
        "grade": 5,
        "pages": 280,
        "year": 2022
    },
    {
        "title": "Biology",
        "grade": 8,
        "pages": 230,
        "year": 2025
    },
    {
        "title": "Physics",
        "grade": 8,
        "pages": 340,
        "year": 2025
    }
])

print("Books for grades 5-8:")
for book in books.find({"grade": {"$gte": 5, "$lte": 8}}):
    print(book)

print("\nBooks published in 2022:")
for book in books.find({"year": 2022}).sort("grade", -1).limit(3):
    print(book)

print("\nBook with the most pages:")
for book in books.find().sort("pages", -1).limit(1):
    print(book)