# Hybrid Cryptography (RSA and Vigenere)

## Description
This is a CLI Python program that encrypts a file using both symmetric and assymmetric cryptography and decypts it vice versa.
* RSA (assymmetric cryptography)
* Vigenere (symmeteric cryptography)

## How to run
1. Download the latest release build of the program
2. Unzip the .zip file to any folder location
3. ...
4. ...
5. Voila, now you can run the program.

## Step by step guide
### Encryption
1. If you have not generated a key pair yet, input `3` on the menu to generate a new key pair.
The key pair will be generated and saved to a default file to the same directory called `private.pen` and `public.pen`
for the private key and public key respectively. 
2. Input `1` on the menu to encrypt
3. Input the file to be encrypted. i.e. `filename.txt`
4. Input the filename of the public key. i.e. `public.pen`
5. Input any keyword. i.e. `Hello` (Note that the same keyword will be used for decryption)
6. After the process, the file to be encrypted is overwritten with a ciphertext.

### Decryption
1. Input `2` on the menu to decrypt
2. Input the file to be decrypted.
3. Input the filename of the private key. i.e. `private.pen`
4. Input the same keyword used on encryption.
5. After the process, if both keys are correct, the file with the ciphertext is overwritten with the original text.


## Algorithms used
### RSA keys
* A public key and a private key will be required for the encryption and decryption of files.
* The public key is used for encrypting a message such that it can only be read by the owner of the private key.
As such it’s also referred to as the encryption key. Decrypting a message can only be done using the private key, hence it’s also called the decryption key.
* Generating a key pair may take a long time depending on the number of bits required. In our case, the program uses `1024 bits`. The bits determine the strength of the key, the same as well can be said to the size of the message.
* After the generation, the keys will be stored in a newly created file called `private.pen` and `public.pen`. You can rename the file to whatever you want.

### Vigenere cipher
* 

### RSA cipher
*

## Process
### Encryption
1.
2.


### Decryption
1.
2.


### Dependencies
* Python 3.0 >
* `pip install rsa`
