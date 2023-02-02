import numpy as np
from sympy import Matrix
import re
import utilities

# import sys
# sys.path.append("../src")
# import utilities

alphabets = [chr(65 + i) for i in range(26)]
N = 26

def encrypt(plainText, keyMatrix):
    print("1", keyMatrix)
    keyMatrixSize, _ = keyMatrix.shape
    arrayText, formatText = preprocess(plainText, keyMatrixSize)
    print("2", arrayText)
    cipherText = ""

    for letter in arrayText:
        current = []
        for i in range(keyMatrixSize):
            current.append(alphabets.index(letter[i]))
        
        encryptCurr = np.matmul(keyMatrix, np.array(current)).tolist()
        for i in range(keyMatrixSize):
            cipherText += alphabets[encryptCurr[i] % 26]

    result = {
        "plainText": formatText,
        "cipherText": cipherText,
        "arrangedCipherText": utilities.arrangeText(cipherText)
    }

    utilities.writeText(cipherText, "../data/output/hill-cipher.txt")
    return result

def decrypt(cipherText, keyMatrix):
    keyMatrixSize, _ = keyMatrix.shape
    arrayCipherText, formatCipherText = preprocess(cipherText, keyMatrixSize)
    inverse = inverseModMatrix(keyMatrix)
    decryptedText = ""

    for letter in arrayCipherText:
        current = []
        for i in range(keyMatrixSize):
            current.append(alphabets.index(letter[i]))
        
        encryptCurr = np.matmul(inverse, np.array(current)).tolist()
        for i in range(keyMatrixSize):
            decryptedText += alphabets[encryptCurr[i] % 26]

    result = {
        "cipherText": formatCipherText,
        "plainText": decryptedText,
    }

    return result

def preprocess(text: str, keyMatrixSize: int):
    formatText = utilities.formatText(text)
    if(len(formatText) % keyMatrixSize != 0):
        formatText += 'X' * (keyMatrixSize - (len(formatText) % keyMatrixSize))
    array = [formatText[i:i+keyMatrixSize] for i in range(0, len(formatText), keyMatrixSize)]
    return array, formatText

def inverseModMatrix(keyMatrix):
    keyMatrixSize, _ = keyMatrix.shape
    preInverse1 = keyMatrix.flatten().tolist()
    preInverse2 = Matrix(keyMatrixSize, keyMatrixSize, preInverse1)
    preInverse3 = preInverse2.inv_mod(26)
    inversed = np.array(preInverse3)
    return inversed

def generateKeyMatrix(plainKey: str, n) -> np.ndarray:
    formatKey = re.sub("[^0-9|,]", "", plainKey)
    formatKey = re.sub(",", " ", formatKey)
    formatKey = list(map(int, formatKey.split()))
    keyMatrix = np.array(formatKey).reshape(n, n)

    return keyMatrix

def keycheck(key):
    det = int(np.linalg.det(key))
    try :
        pow(det, -1, N)
    except ValueError:
        return False
    return det != 0

if __name__ == "__main__":
    print("\n*** Hill Cipher ***\n")
    plainText = input("Plain text: ")
    keyMatrixSize = int(input("> Enter the number of linear equation (matrix size): "))
    print("> Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    keyMatrix = generateKeyMatrix(entries, keyMatrixSize)

    print("\n>>>  Encrypt <<<")
    result = encrypt(plainText, keyMatrix)
    print(result["plainText"], len(result["plainText"]))
    print(result["cipherText"], len(result["cipherText"]))
    print(result["arrangedCipherText"], len(result["arrangedCipherText"]))
    
    print("\n>>>  Decrypt <<<")
    result = decrypt(result["cipherText"], keyMatrix)
    print(result["cipherText"], len(result["cipherText"]))
    print(result["plainText"], len(result["plainText"]), "\n")

# 6 24 1 13 16 10 20 17 15