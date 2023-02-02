import sys

sys.path.append("../src")
import utilities

alphabets = [chr(65 + i) for i in range(26)]

def encrypt(plainText: str, plainKey: str) -> str:
    formatText = utilities.formatText(plainText)
    formatKey = utilities.formatText(plainKey)
    fullKey = generateFullKey(formatText, formatKey)
    
    cipherText = ""
    for i in range(len(formatText)):
        currFormatTextNum = ord(formatText[i]) - ord('A')
        currfullKeyNum = ord(fullKey[i]) - ord('A')
        currCipherTextNum = (currFormatTextNum + currfullKeyNum) % 26
        cipherText += alphabets[currCipherTextNum]

    result = {
        "formatText": formatText,
        "formatKey": formatKey,
        "cipherText": cipherText,
        "arrangedCipherText": utilities.arrangeText(cipherText)
    }
    
    utilities.writeText(cipherText, "../data/output/standard-vigenere-cipher.txt")
    return result

def decrypt(plainCipherText: str, plainKey: str) -> str:
    formatCipherText = utilities.formatText(plainCipherText)
    formatKey = utilities.formatText(plainKey)
    fullKey = generateFullKey(formatCipherText, formatKey)
    
    decryptedText = ""
    for i in range(len(formatCipherText)):
        currFormatCipherTextNum = ord(formatCipherText[i]) - ord('A')
        currFullKeyNum = ord(fullKey[i]) - ord('A')
        currDecryptedTextNum = (currFormatCipherTextNum - currFullKeyNum) % 26
        decryptedText += alphabets[currDecryptedTextNum]

    result = {
        "decryptedText": decryptedText,
        "formatKey": formatKey,
        "cipherText": formatCipherText
    }
    
    return result

def generateFullKey(formatText: str, formatKey: str) -> str:
    if(len(formatKey) >= len(formatText)):
        return formatKey[:len(formatKey)]

    fullKey = formatKey
    for i in range(len(formatText) - len(formatKey)):
        fullKey += formatKey[i % len(formatKey)]
    return fullKey

if __name__ == "__main__":
    plainText = input("> Plain text: ")
    plainKey = input("> Key: ")

    # Standard Vigenere Cipher
    print("\n*** Standard Vigenere Cipher ***")
    result = encrypt(plainText, plainKey)
    print("\n>>>  Encrypt <<<")
    print(result["formatText"], len(result["formatText"]))
    print(result["formatKey"], len(result["formatKey"]))
    print(result["cipherText"], len(result["cipherText"]))
    print(result["arrangedCipherText"], len(result["arrangedCipherText"]))

    result = decrypt(result["cipherText"], plainKey)
    print("\n>>>  Decrypt <<<")
    print(result["cipherText"], len(result["cipherText"]))
    print(result["formatKey"], len(result["formatKey"]))
    print(result["decryptedText"], len(result["decryptedText"]), "\n")