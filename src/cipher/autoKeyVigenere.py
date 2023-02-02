import sys

sys.path.append("../src")
import utilities

def encrypt(plainText: str, plainKey: str) -> str:
    formatText = utilities.formatText(plainText)
    formatKey = utilities.formatText(plainKey)
    keyLength = len(formatKey)

    cipherText = ""
    i = 0
    for letter in formatText:
        if i >= keyLength:
            cipherText += utilities.shiftAlphabet(letter, formatText[i - keyLength], '+')
        else:
            cipherText += utilities.shiftAlphabet(letter, formatKey[i], '+')
        i += 1

    result = {
        "formatText": formatText,
        "formatKey": formatKey,
        "cipherText": cipherText,
        "arrangedCipherText": utilities.arrangeText(cipherText)
    }

    utilities.writeText(cipherText, "../data/output/autokey-vigenere-cipher.txt")
    return result

def decrypt(plainCipherText: str, plainKey: str) -> str:
    formatCipherText = utilities.formatText(plainCipherText)
    formatKey = utilities.formatText(plainKey)
    keyLength = len(formatKey)

    decryptedText = ""
    i = 0
    for letter in formatCipherText:
        if i >= keyLength:
            decryptedText += utilities.shiftAlphabet(letter, decryptedText[i - keyLength], '-')
        else:
            decryptedText += utilities.shiftAlphabet(letter, formatKey[i], '-')
        i += 1

    result = {
        "decryptedText": decryptedText,
        "formatKey": formatKey,
        "cipherText": formatCipherText
    }

    return result

if __name__ == "__main__":
    plainText = input("> Plain text: ")
    plainKey = input("> Key: ")

    # Autokey Vigenere Cipher
    print(f"\n*** Autokey Vigenere Cipher ***")
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