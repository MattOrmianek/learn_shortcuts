
# TODO: create a structured database from the input data
# Structure of shortcuts table:
# - id - actual shortcut - description - date_of_creation - date_of_last_usage - usage_count

# Structure of games table:
# - id - points - ids of shortcuts - mode - rounds - date - time

# TODO: add to a structured database new data

# TODO: choose db to use
# TODO: create tables
# TODO: create script for creating db from 0, for test  - create_db_from_zero.py
# TODO: create connecting to db
# TODO: create script for adding data to db - add_data_to_db.py
# TODO: create CRUD operations for db

import time
from pymongo import MongoClient

# Connect to the MongoDB server running on localhost:27017 (default)
client = MongoClient('mongodb://localhost:27017/')

db = client['learn_shortcuts']

collection = db['shortcuts']

# This is example of one row in shortcuts table
class shortcuts_table_object:
    def __init__(self, id, shortcut, description, date_of_creation, date_of_last_usage, usage_count):
        self.id = id
        self.shortcut = shortcut
        self.description = description
        self.date_of_creation = date_of_creation
        self.date_of_last_usage = date_of_last_usage
        self.usage_count = usage_count
    def __str__(self):
        return f"{self.id} {self.shortcut} {self.description} {self.date_of_creation} {self.date_of_last_usage} {self.usage_count}"
    def to_dict(self):
        return {
        "id": self.id,
        "shortcut": self.shortcut,
        "description": self.description,
        "date_of_creation": self.date_of_creation,
        "date_of_last_usage": self.date_of_last_usage,
        "usage_count": self.usage_count
        }
try:
    first_shortcut = shortcuts_table_object(0, "Ctrl + C", "Copy", time.time(), time.time(), 0)
    collection.insert_one(first_shortcut.to_dict())
except Exception as error:
    print(error)

print(collection.find_one({"id": 0}))
