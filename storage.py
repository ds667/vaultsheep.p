import json
import os
from encryption import encrypt_message, decrypt_message

STORAGE_FILE = "vaultsheep_storage.json"

def load_storage():
    if not os.path.exists(STORAGE_FILE):
        return {"passwords": {}, "diary": []}
    with open(STORAGE_FILE, "r") as file:
        return json.load(file)

def save_storage(data):
    with open(STORAGE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_password(site, username, password):
    data = load_storage()
    encrypted_password = encrypt_message(password)
    data["passwords"][site] = {"username": username, "password": encrypted_password}
    save_storage(data)

def get_password(site):
    data = load_storage()
    if site in data["passwords"]:
        entry = data["passwords"][site]
        decrypted_password = decrypt_message(entry["password"])
        return entry["username"], decrypted_password
    return None

def delete_password(site):
    data = load_storage()
    if site in data["passwords"]:
        del data["passwords"][site]
        save_storage(data)

def add_diary_entry(entry):
    data = load_storage()
    encrypted_entry = encrypt_message(entry)
    data["diary"].append(encrypted_entry)
    save_storage(data)

def get_diary_entries():
    data = load_storage()
    return [decrypt_message(entry) for entry in data["diary"]]

def delete_diary_entry(index):
    data = load_storage()
    if 0 <= index < len(data["diary"]):
        del data["diary"][index]
        save_storage(data)

if __name__ == "__main__":
    add_password("github.com", "sheepMaster", "supersecret123")
    print(get_password("github.com"))

    add_diary_entry("Today, I protected my passwords like a pro!")
    print(get_diary_entries())
