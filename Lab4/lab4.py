import os
import time
import hashlib
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hmac

# Generate AES key
def generate_aes_key(key_size):
    return os.urandom(key_size // 8)

# Function to generate RSA keys
def generate_rsa_keys(key_size):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Save private key
    with open("rsa_private_key.pem", "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    # Save public key
    with open("rsa_public_key.pem", "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

# AES encryption/decryption
# AES encryption/decryption
def aes_encrypt_decrypt(input_file, output_file, key, mode, iv=None, encrypt=True):
    backend = default_backend()
    block_size = algorithms.AES.block_size

    if mode == 'ECB':
        cipher_mode = modes.ECB()
    elif mode == 'CFB':
        if encrypt:
            if iv is None:
                iv = os.urandom(16)
            cipher_mode = modes.CFB(iv)
        else:
            with open(input_file, 'rb') as f:
                iv = f.read(16)
                ciphertext = f.read()
            cipher_mode = modes.CFB(iv)
    
    cipher = Cipher(algorithms.AES(key), cipher_mode, backend=backend)

    if encrypt:
        encryptor = cipher.encryptor()
        padder = sym_padding.PKCS7(block_size).padder()

        with open(input_file, 'rb') as f:
            plaintext = f.read()

        padded_plaintext = padder.update(plaintext) + padder.finalize()
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

        with open(output_file, 'wb') as f:
            if mode == 'CFB':
                f.write(iv)
            f.write(ciphertext)
    else:
        decryptor = cipher.decryptor()
        unpadder = sym_padding.PKCS7(block_size).unpadder()

        with open(input_file, 'rb') as f:
            if mode != 'CFB':
                ciphertext = f.read()
            # No need to re-read the file here, already read above
            # ciphertext = f.read()
        
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        with open(output_file, 'wb') as f:
            f.write(plaintext)


# RSA encryption/decryption
def rsa_encrypt_decrypt(input_file, output_file, public_key_file, private_key_file, encrypt=True):
    with open(input_file, 'rb') as f:
        data = f.read()

    if encrypt:
        with open(public_key_file, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

        ciphertext = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open(output_file, 'wb') as f:
            f.write(ciphertext)
    else:
        with open(private_key_file, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        plaintext = private_key.decrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open(output_file, 'wb') as f:
            f.write(plaintext)

# RSA signature
def rsa_sign_verify(input_file, signature_file, private_key_file=None, public_key_file=None, sign=True):
    if sign:
        with open(private_key_file, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        with open(input_file, 'rb') as f:
            data = f.read()

        signature = private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        with open(signature_file, 'wb') as f:
            f.write(signature)
    else:
        with open(public_key_file, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )

        with open(input_file, 'rb') as f:
            data = f.read()

        with open(signature_file, 'rb') as f:
            signature = f.read()

        try:
            public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print("Verification successful")
        except Exception as e:
            print("Verification failed:", e)

# SHA-256 hashing
def sha256_hash(input_file):
    sha256 = hashlib.sha256()

    with open(input_file, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256.update(byte_block)

    print("SHA-256 hash:", sha256.hexdigest())

# Menu and main functionality
def main():
    while True:
        print("\nChoose an option:")
        print("1. Generate AES Key")
        print("2. Generate RSA Keys")
        print("3. AES Encrypt/Decrypt")
        print("4. RSA Encrypt/Decrypt")
        print("5. RSA Sign/Verify")
        print("6. SHA-256 Hash")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key_size = int(input("Enter key size (128/256): "))
            key = generate_aes_key(key_size)
            with open("aes_key.bin", "wb") as key_file:
                key_file.write(key)
            print(f"AES key of size {key_size} bits generated and saved as 'aes_key.bin'.")
        elif choice == 2:
            key_size = int(input("Enter key size: "))
            generate_rsa_keys(key_size)
            print(f"RSA keys of size {key_size} bits generated and saved as 'rsa_private_key.pem' and 'rsa_public_key.pem'.")
        elif choice == 3:
            key_file = input("Enter key file: ")
            input_file = input("Enter input file: ")
            output_file = input("Enter output file: ")
            key_size = int(input("Enter key size (128/256): "))
            mode = input("Enter mode (ECB/CFB): ")
            encrypt = int(input("Encrypt (1) or Decrypt (0): "))

            with open(key_file, "rb") as f:
                key = f.read()

            iv = None
            if mode == "CFB" and encrypt:
                iv = os.urandom(16)
                print("IV generated for CFB mode.")

            start_time = time.time()
            aes_encrypt_decrypt(input_file, output_file, key, mode, iv, encrypt)
            end_time = time.time()
            print(f"AES {mode} {'encryption' if encrypt else 'decryption'} completed in {end_time - start_time:.4f} seconds.")
        elif choice == 4:
            public_key_file = input("Enter public key file: ")
            private_key_file = input("Enter private key file: ")
            input_file = input("Enter input file: ")
            output_file = input("Enter output file: ")
            encrypt = int(input("Encrypt (1) or Decrypt (0): "))

            start_time = time.time()
            rsa_encrypt_decrypt(input_file, output_file, public_key_file, private_key_file, encrypt)
            end_time = time.time()
            print(f"RSA {'encryption' if encrypt else 'decryption'} completed in {end_time - start_time:.4f} seconds.")
        elif choice == 5:
            private_key_file = input("Enter private key file: ")
            public_key_file = input("Enter public key file: ")
            input_file = input("Enter input file: ")
            signature_file = input("Enter signature file: ")
            sign = int(input("Sign (1) or Verify (0): "))

            start_time = time.time()
            rsa_sign_verify(input_file, signature_file, private_key_file, public_key_file, sign)
            end_time = time.time()
            print(f"RSA {'signing' if sign else 'verification'} completed in {end_time - start_time:.4f} seconds.")
        elif choice == 6:
            input_file = input("Enter input file: ")
            start_time = time.time()
            sha256_hash(input_file)
            end_time = time.time()
            print(f"SHA-256 hashing completed in {end_time - start_time:.4f} seconds.")
        elif choice == 7:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
