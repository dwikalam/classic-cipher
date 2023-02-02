import utilities
from cipher import standardVigenere as svc

# if __name__ == __main__
# import sys
# import standardVigenere as svc
# sys.path.append("../src")
# import utilities

BYTE_MAX = 256

def encrypt(srcPath: str, plainKey: str, encDestPath: str) -> bool:
    try:
        file = open(srcPath, 'rb')
        fileData = bytearray(file.read())
        fullKey = svc.generateFullKey(fileData, utilities.formatText(plainKey))
        for idx, plainText in enumerate(fileData):
            fileData[idx] = (plainText + ord(fullKey[idx])) % BYTE_MAX
        file.close()

        file = open(encDestPath, 'wb')
        file.write(fileData)
        file.close()

        result = {
            "filePath": srcPath,
            "destPath": encDestPath
        }
        return result
        
    except Exception as err:
        return {}

def decrypt(encSrcPath: str, plainKey: str, decDestPath: str) -> str :
    try:
        file = open(encSrcPath, 'rb')
        fileData = bytearray(file.read())
        fullKey = svc.generateFullKey(fileData, utilities.formatText(plainKey))
        for idx, cipherText in enumerate(fileData):
            fileData[idx] = (cipherText - ord(fullKey[idx])) % BYTE_MAX
        file.close()

        file = open(decDestPath, 'wb')
        file.write(fileData)
        file.close()

        result = {
            "plainText": fileData,
            
            "filePath": encSrcPath,
            "destPath": decDestPath
        }
        return result

    except Exception as err:
        return {}

if __name__ == "__main__":
    # srcPath = input("> Source File Path: ")
    # plainKey = input("> Key: ")
    # encryptionPath = input("> Encrypted File Destionation Path: ")
    # decryptionPath = input("> Decrypted File Destination Path: ")
    srcPath = "../data/input/plainText.txt"
    plainKey = "cidmath"
    encryptedPath = "../data/output/extended-vigenere/encrypted-plainText.txt"
    decryptedPath = "../data/output/extended-vigenere/decrypted-plainText.txt"

    print("\n*** Extended Vigenere Cipher ***")
    _ = encrypt(srcPath, plainKey, encryptedPath)
    _ = decrypt(encryptedPath, plainKey, decryptedPath)
    print("Successful!")
    print()

# Source File Directory: "../data/input/"
# Encrypted File Destination Directory: "../data/output/"
# Decrypted File Destination Directory: "../data/output/"