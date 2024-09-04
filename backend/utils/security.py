import hashlib
import os
import re
from cryptography.fernet import Fernet
from flask import current_app as app

# Generate a key for encryption and decryption
def generate_key():
    """Generate a new key for encryption and decryption."""
    return Fernet.generate_key().decode()

# Load the encryption key from the environment variable or generate a new one
def get_key():
    """Retrieve the encryption key from environment variables or generate a new one."""
    key = os.getenv('ENCRYPTION_KEY')
    if not key:
        key = generate_key()
        # Ideally, save this key securely (e.g., in a secrets manager)
        app.logger.info("No encryption key found, generated a new one.")
    return key.encode()

# Initialize Fernet for encryption/decryption
def get_fernet():
    """Initialize and return a Fernet instance with the encryption key."""
    return Fernet(get_key())

# Hash a password using SHA-256
def hash_password(password: str) -> str:
    """Hash a password using SHA-256."""
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

# Verify a password against a hashed password
def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password."""
    return hash_password(password) == hashed_password

# Validate email format
def validate_email(email: str) -> bool:
    """Check if the provided email address is in a valid format."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Encrypt a piece of data
def encrypt_data(data: str) -> str:
    """Encrypt data using Fernet encryption."""
    fernet = get_fernet()
    encrypted_data = fernet.encrypt(data.encode()).decode()
    return encrypted_data

# Decrypt a piece of data
def decrypt_data(encrypted_data: str) -> str:
    """Decrypt data using Fernet encryption."""
    fernet = get_fernet()
    decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()
    return decrypted_data

# Example of how to use these functions
if __name__ == "__main__":
    sample_password = "my_secure_password"
    hashed = hash_password(sample_password)
    print(f"Hashed Password: {hashed}")
    print(f"Password Verified: {verify_password(sample_password, hashed)}")

    email = "test@example.com"
    print(f"Is Email Valid: {validate_email(email)}")

    data = "Sensitive Information"
    encrypted = encrypt_data(data)
    print(f"Encrypted Data: {encrypted}")
    decrypted = decrypt_data(encrypted)
    print(f"Decrypted Data: {decrypted}")

