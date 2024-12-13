from cryptography.fernet import Fernet
def encrypt():
    message = input("enter message: ")
    key = Fernet.generate_key()
    print(str(key))

    fernet = Fernet(key)

    encmessage = fernet.encrypt(message.encode())

    print("original string: ", message)
    print("encrypted message: ", encmessage)

def decrypt():
    message = input("Enter encrypted message: ")
    key = input("Enter key: ")
    fernet = Fernet(key)
    decmessage = fernet.decrypt(message).decode()
    print("decrypted string: ", decmessage)
print("Enter ENCRYPT to encrypt a message")
print("Enter DECRYPT to decrypt a message")
option = input("Enter option: ")
if option == "ENCRYPT":
    encrypt()
if option == "DECRYPT":
    decrypt()