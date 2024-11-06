# Command-Line Password Manager

A simple, secure password manager that runs on the command line, allowing you to securely store, retrieve, delete, and generate account passwords. Passwords are encrypted and stored in a JSON file (`passwords.json`), and the encryption key is saved in `secret.key` to ensure security.

## Features

- **Add Account Passwords**: Save a new encrypted password for an account.
- **Retrieve Account Passwords**: Retrieve a saved password in decrypted form.
- **Delete Account Passwords**: Delete a saved account’s password.
- **Generate Secure Passwords**: Generate a strong, random password with customizable length.

## Project Files

- **`password_manager.py`**: The main program file. This script contains all functionality and serves as the command-line interface for the password manager.
- **`passwords.json`**: The JSON file where all encrypted account passwords are stored. The file is created automatically if it doesn’t exist.
- **`secret.key`**: A file that stores the encryption key used to encrypt and decrypt passwords. This file is generated on the first run.

## Security

Passwords are securely encrypted using the `cryptography` library’s `Fernet` encryption, ensuring that even if `passwords.json` is accessed directly, the passwords cannot be read without the `secret.key` file.

> **Note**: Make sure to keep `secret.key` in a secure location, as it is required to decrypt your passwords. Losing this file means you will not be able to access any stored passwords.

## Requirements

- Python 3.6+
- Required libraries can be installed using the `requirements.txt` file.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
