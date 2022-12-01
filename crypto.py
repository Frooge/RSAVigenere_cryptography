import rsa


def menu():
    print("Hybrid Cryptography (RSA and Vigenere)\n1 : encrypt\n2 : decrypt\n3 : generate rsa key pair\n4 : exit")
    choice = input("Choice: ")
    return choice


def generate_key_pair():
    (public_key, private_key) = rsa.newkeys(1024)
    save_key_file(private_key, "private.pen")
    save_key_file(public_key, "public.pen")
    print("Successfully generate key pair!")


def save_file(content, file_name, mode):
    with open(file_name, mode) as f:
        f.write(content)
    f.close()


def open_file(file_name, mode):
    with open(file_name, mode) as f:
        return f.read()


def save_key_file(key, file_name):
    with open(file_name, 'wb') as f:
        f.write(rsa.PrivateKey.save_pkcs1(key))
    f.close()


def open_key_file(key_mode, file_name):
    with open(file_name, 'rb') as f:
        key_data = f.read()
        if key_mode == 'private':
            return rsa.PrivateKey.load_pkcs1(key_data)
        elif key_mode == 'public':
            return rsa.PublicKey.load_pkcs1(key_data)


def encrypt():
    file_name = input("Input filename: ")
    text = open_file(file_name, 'r')
    key_file_name = input("Input rsa public key filename: ")
    key = open_key_file("public", key_file_name)
    keyword = input("Input keyword: ")
    text = vigenere(text, keyword, 'encrypt')
    cipher = rsa.encrypt(text.encode('utf-8'), key)
    save_file(cipher, file_name, 'wb')
    print("Successfully encrypted file!")


def decrypt():
    file_name = input("Input filename: ")
    text = open_file(file_name, 'rb')
    key_file_name = input("Input rsa private key filename: ")
    key = open_key_file("private", key_file_name)
    keyword = input("Input keyword: ")
    plain = rsa.decrypt(text, key)
    plain = vigenere(plain.decode('utf-8'), keyword, 'decrypt')
    save_file(plain, file_name, 'w')
    print("Successfully decrypted file!")


def vigenere(text, keyword, mode):
    converted = list()
    key_size = len(keyword)
    if mode == 'encrypt':
        for idx, c in enumerate(text):
            converted.append(chr(ord(c) + ord(keyword[idx % key_size])))
    elif mode == 'decrypt':
        for idx, c in enumerate(text):
            converted.append(chr(ord(c) - ord(keyword[idx % key_size])))
    converted = ''.join(converted)
    return converted


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
