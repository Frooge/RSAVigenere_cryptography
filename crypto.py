import rsa


def menu():
    print("Hybrid Cryptography (RSA and Vigenere)\n1 : encrypt\n2 : decrypt\n3 : generate rsa key pair\n4 : exit")
    choice = input("Choice: ")
    return choice


def generate_key_pair():
    (public_key, private_key) = rsa.newkeys(1024)
    save_key_file(private_key, "private_key.pen")
    save_key_file(public_key, "public_key.pen")
    print("Successfully generate key pair!")


def save_file(text, file_name, mode):
    try:
        with open(file_name, mode) as f:
            f.write(text)
        f.close()
    except IOError as e:
        print(e)


def open_file(file_name, mode):
    try:
        with open(file_name, mode) as f:
            return f.read()
    except IOError as e:
        print(e)


def save_key_file(key, file_name):
    try:
        with open(file_name, 'wb') as f:
            f.write(rsa.PrivateKey.save_pkcs1(key))
        f.close()
    except IOError as e:
        print(e)


def open_key_file(key_mode, file_name):
    try:
        with open(file_name, 'rb') as f:
            key_data = f.read()
            if key_mode == 'private':
                return rsa.PrivateKey.load_pkcs1(key_data)
            elif key_mode == 'public':
                return rsa.PublicKey.load_pkcs1(key_data)
    except IOError as e:
        print(e)


def rsa_encrypt(text, key):
    return rsa.encrypt(text.encode('utf-8'), key)


def rsa_decrypt(text, key):
    return rsa.decrypt(text, key).decode('utf-8')


def vigenere_encrypt(text, keyword):
    output = ""
    key_size = len(keyword)
    for idx, c in enumerate(text):
        output += chr(ord(c) + ord(keyword[idx % key_size]))
    return output


def vigenere_decrypt(text, keyword):
    output = ""
    key_size = len(keyword)
    for idx, c in enumerate(text):
        output += chr(ord(c) - ord(keyword[idx % key_size]))
    return output


def encrypt():
    file_name = input("Input filename: ")
    text = open_file(file_name, "r")
    key_file_name = input("Input rsa public key filename: ")
    key = open_key_file("public", key_file_name)
    keyword = input("Input keyword: ")

    text = vigenere_encrypt(text, keyword)
    cipher = rsa_encrypt(text, key)

    save_file(cipher, file_name, "wb")

    print("Successfully encrypted file!")


def decrypt():
    file_name = input("Input filename: ")
    text = open_file(file_name, "rb")
    key_file_name = input("Input rsa private key filename: ")
    key = open_key_file("private", key_file_name)
    keyword = input("Input keyword: ")

    text = rsa_decrypt(text, key)
    plain = vigenere_decrypt(text, keyword)

    save_file(plain, file_name, "w")
    print("Successfully decrypted file!")


if __name__ == '__main__':
    flag = 1
    while flag:
        answer = menu()
        if answer == '1':
            encrypt()
        elif answer == '2':
            decrypt()
        elif answer == '3':
            generate_key_pair()
        else:
            flag = 0
