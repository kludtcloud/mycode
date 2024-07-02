from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

# Function to derive a key from a password using SHA-256
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

# Function to encrypt data
def encrypt_data(data: bytes, password: str) -> bytes:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return b64encode(salt + iv + encrypted)

# Function to read from a file and encrypt its content
def encrypt_file(input_file: str, output_file: str, password: str):
    with open(input_file, 'rb') as f:
        data = f.read()

    encrypted_data = encrypt_data(data, password)

    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

    print(f"File '{input_file}' has been encrypted and saved as '{output_file}'.")

# Function to decrypt data
def decrypt_data(encrypted_data: bytes, password: str) -> bytes:
    data = b64decode(encrypted_data)
    salt, iv, encrypted = data[:16], data[16:32], data[32:]
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

# Function to read from an encrypted file and decrypt its content
def decrypt_file(input_file: str, output_file: str, password: str):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_data(encrypted_data, password)

    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print(f"File '{input_file}' has been decrypted and saved as '{output_file}'.")

# Usage example
password = "strongpassword"
input_file = "input.txt"
encrypted_file = "encrypted_output.txt"
decrypted_file = "decrypted_output.txt"

# Encrypt the file
encrypt_file(input_file, encrypted_file, password)

# Decrypt the file (optional step to verify)
decrypt_file(encrypted_file, decrypted_file, password)