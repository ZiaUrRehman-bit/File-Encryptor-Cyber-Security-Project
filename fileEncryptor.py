from cryptography.fernet import Fernet

def generateKey():
    return Fernet.generate_key()

def saveKey(key, keyFile):
    with open(keyFile, 'wb') as file:
        file.write(key)

def loadKey(keyFile):
    with open(keyFile, 'rb') as file:
        return file.read()
    
def encryptFile(inputFile, outputFile, key):
    with open(inputFile, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encryptData = fernet.encrypt(data)

    with open(outputFile, 'wb') as file:
        file.write(encryptData)

def decryptFile(inputFile, outputFile, key):
    with open(inputFile, 'rb') as file:
        encryptedData = file.read()

    fernet = Fernet(key)
    decryptedData = fernet.decrypt(encryptedData)

    with open(outputFile, 'wb') as file:
        file.write(decryptedData)

if __name__ == "__main__":

    key = generateKey()
    keyFile = 'encyrptionKey.key'
    saveKey(key, keyFile)

    inputFile = 'plaintext.txt'
    encryptedFile = 'encryptedFile.txt'
    decryptedFile = 'decryptedFile.txt'

    encryptFile(inputFile, encryptedFile, key)
    print(f"File '{inputFile}' encrypted to '{encryptedFile}'")

    decryptFile(encryptedFile, decryptedFile, key)
    print(f"File '{encryptedFile}' encrypted to '{decryptedFile}'")