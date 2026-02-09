import json
import os
from config import PACKAGES_FILE

DB_FILE = "database.json"

def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({"users": []}, f)
    with open(DB_FILE) as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Tambah transaksi user
def add_user_transaction(user_id, name, package, deposit, profit):
    db = load_db()
    for u in db["users"]:
        if u["user_id"] == user_id and u["status"] == "pending":
            return False
    db["users"].append({
        "
