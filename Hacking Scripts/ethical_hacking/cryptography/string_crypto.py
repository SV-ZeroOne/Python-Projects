#pip3 install cryptography

from cryptography.fernet import Fernet

if __name__ == "__main__":
    key = Fernet.generate_key()
    print(key)
    message = "This is my secret message"
    msg_bin = message.encode()
    #print(msg_bin)
    f = Fernet(key)
    encrypted_msg = f.encrypt(msg_bin)
    print(encrypted_msg)
    decrypted_msg = f.decrypt(encrypted_msg)
    print(decrypted_msg)