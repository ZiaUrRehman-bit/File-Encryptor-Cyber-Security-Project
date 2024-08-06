from cryptography.fernet import Fernet  # Import the Fernet class from the cryptography library for encryption and decryption.

def generateKey():
    # Function to generate a new Fernet key.
    return Fernet.generate_key()

def saveKey(key, keyFile):
    # Function to save the generated key to a file.
    with open(keyFile, 'wb') as file:  # Open the specified file in binary write mode.
        file.write(key)  # Write the key to the file.

def loadKey(keyFile):
    # Function to load a key from a file.
    with open(keyFile, 'rb') as file:  # Open the specified file in binary read mode.
        return file.read()  # Read and return the key from the file.

def encryptFile(inputFile, outputFile, key):
    # Function to encrypt the contents of a file.
    with open(inputFile, 'rb') as file:  # Open the input file in binary read mode.
        data = file.read()  # Read the data from the file.

    fernet = Fernet(key)  # Create a Fernet object with the given key.
    encryptData = fernet.encrypt(data)  # Encrypt the data using the Fernet object.

    with open(outputFile, 'wb') as file:  # Open the output file in binary write mode.
        file.write(encryptData)  # Write the encrypted data to the output file.

def decryptFile(inputFile, outputFile, key):
    # Function to decrypt the contents of a file.
    with open(inputFile, 'rb') as file:  # Open the input file (encrypted) in binary read mode.
        encryptedData = file.read()  # Read the encrypted data from the file.

    fernet = Fernet(key)  # Create a Fernet object with the given key.
    decryptedData = fernet.decrypt(encryptedData)  # Decrypt the data using the Fernet object.

    with open(outputFile, 'wb') as file:  # Open the output file in binary write mode.
        file.write(decryptedData)  # Write the decrypted data to the output file.

if __name__ == "__main__":
    # Main function to execute when the script is run.

    key = generateKey()  # Generate a new encryption key.
    keyFile = 'encyrptionKey.key'  # Define the file name to save the key.
    saveKey(key, keyFile)  # Save the generated key to a file.

    inputFile = 'plaintext.txt'  # Define the name of the input file to be encrypted.
    encryptedFile = 'encryptedFile.txt'  # Define the name of the output file to store encrypted data.
    decryptedFile = 'decryptedFile.txt'  # Define the name of the output file to store decrypted data.

    encryptFile(inputFile, encryptedFile, key)  # Encrypt the input file and save it to the encrypted file.
    print(f"File '{inputFile}' encrypted to '{encryptedFile}'")  # Print confirmation message for encryption.

    decryptFile(encryptedFile, decryptedFile, key)  # Decrypt the encrypted file and save it to the decrypted file.
    print(f"File '{encryptedFile}' decrypted to '{decryptedFile}'")  # Print confirmation message for decryption.
