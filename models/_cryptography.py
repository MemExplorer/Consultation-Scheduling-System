from cryptography.fernet import Fernet

# generate a key for encryption and decryption
# You can use fernet to generate
# the key or use random key generator
# here I'm using fernet to generate key
 
# Static key generated using Fernet.generate_key(), not applicable for production purposes.
_key = b'k4hpuVzgUjBleIOCnnoZ3kkCI7xFPPBfL4NdFTgCbs4='

class Security(Fernet):
    

    def __init__(self):
        super().__init__(_key)

    def Encrypt(self, text:str) -> str:
        encrypt = self.encrypt(text.encode())
        return encrypt
    
    def Decrypt(self, text:str) -> str:
        decode = self.decrypt(text).decode()
        return decode


# Manual Testing

if __name__ == "__main__":
    _instance = Security()
    print(_key)
    print(_instance.Encrypt("test"))
    print(_instance.Decrypt(_instance.Encrypt("test")))