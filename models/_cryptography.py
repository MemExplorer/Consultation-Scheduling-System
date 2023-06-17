from cryptography.fernet import Fernet
import base64

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key
 
# Static key generated using Fernet.generate_key(), not applicable for production purposes.
_key = b'k4hpuVzgUjBleIOCnnoZ3kkCI7xFPPBfL4NdFTgCbs4='

class Security(Fernet):
    

    def __init__(self):
        super().__init__(_key)

    def Encrypt(self, text:str) -> bytes:
        encrypt = self.encrypt(text.encode())
        return encrypt
    
    def Decrypt(self, text:str) -> str:
        decode = self.decrypt(text).decode()
        return decode


# Manual Testing

if __name__ == "__main__":
    _instance = Security()
    _encrypted = _instance.Encrypt("test")
    _decrypted = _instance.Decrypt(_encrypted)
    _64encrypted = base64.b64encode(_encrypted).decode()
    _64decrpyted = base64.b64decode(_64encrypted).decode()
    print()
    print(f"Static Key Generated: {_key}")
    print(f"Encrypted Password using only Fernet Cryptography (byte): {_encrypted}") # passed
    print(f"Decrpyted Password using only Fernet Cryptography (str): {_decrypted}") # passed
    print(f"Encrypted using both Fernet and Base 64 (str): {_64encrypted}") # passed
    print(f"Decrypted into Fernet cryptography using Base 64 (str): {_64decrpyted}") # passed
    print(f"Decrypted Into str using fernet decryption (str): {_instance.Decrypt(_64decrpyted)}") # passed