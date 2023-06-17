
if __name__ == "__main__":
    _instance = Security()
    print(_key)
    print(_instance.Encrypt("test"))
    print(_instance.Decrypt(_instance.Encrypt("test")))