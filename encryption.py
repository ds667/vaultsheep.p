from cryptography.fernet import Fernet
import os

KEY_FILE = "vaultsheep.key"

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    else:
        raise FileNotFoundError("Encryption key not found! Run generate_key() first.")

def encrypt_message(message: str) -> str:
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt_message(encrypted_message: str) -> str:
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

if __name__ == "__main__":
    generate_key()
    test_message = "VaultSheep protects your secrets!"
    encrypted = encrypt_message(test_message)
    decrypted = decrypt_message(encrypted)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
