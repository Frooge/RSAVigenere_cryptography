import rsa


def generate_key_pair():
    (public_key, private_key) = rsa.newkeys(512)
    save_key_file(private_key, "rsa_pri.bin")
    save_key_file(public_key, "rsa_pub.bin")
    print("Successfully generate key pair!")


def menu():
    print("3105 Project Cryptography\n1 : encrypt\n2 : decrypt\n3 : generate rsa key pair\n4 : exit")
    choice = input("Choice: ")
    return choice


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
    key_file_name = input("Input rsa public key filename: ")
    text = open_file(file_name, 'r')
    key = open_key_file("public", key_file_name)
    cipher = rsa.encrypt(text.encode('utf-8'), key)
    save_file(cipher, file_name, 'wb')
    print("Successfully encrypted file!")


def decrypt():
    file_name = input("Input filename: ")
    key_file_name = input("Input rsa private key filename: ")
    text = open_file(file_name, 'rb')
    key = open_key_file("private", key_file_name)
    plain = rsa.decrypt(text, key)
    save_file(plain.decode('utf-8'), file_name, 'w')
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
