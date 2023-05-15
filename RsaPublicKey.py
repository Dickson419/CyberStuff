import rsa
"""
Asymmetric - encrypt and decrypt with public and private keys
Encrypt with public key for confidentiality 
Decrypt with private key (to rx the message)
Sign with the private key for authenticity
"""

#place keys in variables
publicKey, privateKey = rsa.newkeys(1024) #1024 bytes

def generateKeys(public, private):
    """In a function so keys can be generated once only"""
    """Store keys in PEM. Container to store cryptographic keys (defines structure and encoding type)"""
    with open("public.pem", 'wb') as f:
        f.write(public.save_pkcs1("PEM"))

    with open("private.pem", 'wb') as f:
        f.write(private.save_pkcs1("PEM"))

def encrypt():
    """Files need to be loaded and read with the same algorithm - .read will not work"""
    with open("public.pem", 'rb') as f:
        publicKey = rsa.PublicKey.load_pkcs1(f.read())

    message = "Hello my name is Steven... or is it?"
    encryptedMessage = rsa.encrypt(message.encode(), publicKey)

    """Write encrypted message to a file"""
    with open("Encrypted_message",'wb') as f:
        f.write(encryptedMessage)
    print(encryptedMessage, "\n") #.decode will remove the b in printed text

def decrypt():
    with open("private.pem", 'rb') as f:
        privateKey = rsa.PrivateKey.load_pkcs1(f.read())

    encryptedMessage = open("Encrypted_message", 'rb').read()
    clearMessage = rsa.decrypt(encryptedMessage, privateKey)
    print(clearMessage) #.decode will remove the b in printed text

def signature():
    """Next use case is to check authenticity"""
    message = "New cool account has been made on wicked social media... marketingSucksBalls"
    signature = rsa.sign(message.encode(), privateKey, "SHA-256")

    #write signature to a file
    with open("Signature", 'wb') as f:
        f.write(signature)

    # read message
    with open("Signature", 'rb') as f:
        readSignature = f.read()

    authMessage = rsa.verify(message.encode(), readSignature, publicKey)
    print(authMessage)


encrypt()
decrypt()
signature()
