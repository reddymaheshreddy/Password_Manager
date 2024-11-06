import json
import os
import argparse
from cryptography.fernet import Fernet
import secrets
import string

# Passwords file path
PASSWORD_FILE = 'passwords.json'

# Generate a key for encryption
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

# Encrypt/decrypt functions
fernet = load_key()

def encrypt(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt(text):
    return fernet.decrypt(text.encode()).decode()

# Functions to handle passwords
def add_password(account, username, password=None):
    password = password or generate_password()
    encrypted_password = encrypt(password)
    passwords = load_passwords()
    passwords[account] = {'username': username, 'password': encrypted_password}
    save_passwords(passwords)
    print(f"Password for {account} added.")

def get_password(account):
    passwords = load_passwords()
    if account in passwords:
        entry = passwords[account]
        decrypted_password = decrypt(entry['password'])
        print(f"Account: {account}\nUsername: {entry['username']}\nPassword: {decrypted_password}")
    else:
        print(f"No entry found for {account}.")

def delete_password(account):
    passwords = load_passwords()
    if account in passwords:
        del passwords[account]
        save_passwords(passwords)
        print(f"Password for {account} deleted.")
    else:
        print(f"No entry found for {account}.")

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Load and save functions
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            encrypted_data = file.read()
            if encrypted_data:
                decrypted_data = decrypt(encrypted_data)
                return json.loads(decrypted_data)
    return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        encrypted_data = encrypt(json.dumps(passwords))
        file.write(encrypted_data)

# Main CLI handling with argparse
def main():
    parser = argparse.ArgumentParser(description="Secure Password Manager")
    parser.add_argument("action", choices=["add", "get", "delete", "generate"], help="Action to perform")
    parser.add_argument("--account", help="Account name")
    parser.add_argument("--username", help="Username for the account")
    parser.add_argument("--password", help="Password for the account")
    parser.add_argument("--length", type=int, help="Length of the generated password")

    args = parser.parse_args()

    if args.action == "add":
        if not args.account or not args.username:
            print("Please provide both --account and --username for adding a password.")
        else:
            add_password(args.account, args.username, args.password)

    elif args.action == "get":
        if not args.account:
            print("Please provide --account to retrieve a password.")
        else:
            get_password(args.account)

    elif args.action == "delete":
        if not args.account:
            print("Please provide --account to delete a password.")
        else:
            delete_password(args.account)

    elif args.action == "generate":
        length = args.length if args.length else 12
        password = generate_password(length)
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
