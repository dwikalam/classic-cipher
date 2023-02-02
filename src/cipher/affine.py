# import sys

# sys.path.append("../src")
# import utilities

import utilities

alphabets = [chr(65 + i) for i in range(26)]
N = 26

def encrypt(plainText: str, keyM: int, keyB: int) -> str:
    try:
        _ = pow(keyM, -1, N)
    except ValueError:
        return "primeError"

    cipherText = ""
    formatText = plainText.upper()
    for char in formatText:
        if alphabets.count(char) != 0:
            cipherText += alphabets[(alphabets.index(char) * keyM + keyB) % N]
        else :
            cipherText += char

    result = {
        "plainText": formatText,
        "keyM": keyM,
        "keyB": keyB,
        "cipherText": cipherText,
        "arrangedCipherText": utilities.arrangeText(cipherText)
    }

    utilities.writeText(cipherText, "../data/output/affine-cipher.txt")
    return result

def decrypt(cipherText: str, keyM: int, keyB: int) -> str:
    try:
        dec = pow(keyM, -1, N)
    except ValueError:
        return "primeError"

    decryptedText = ""
    formatCipherText = cipherText.upper()
    for char in formatCipherText:
        if alphabets.count(char) != 0 :
            decryptedText += alphabets[((alphabets.index(char) - keyB) * dec) % N]
        else :
            decryptedText += char

    result = {
        "cipherText": formatCipherText,
        "keyM": keyM,
        "keyB": keyB,
        "plainText": decryptedText
    }

    return result

if __name__ == "__main__":
    plainText = input("> Plain text: ")
    keyM = int(input("> Key M: "))
    keyB = int(input("> Key B: "))

    # Affine Cipher
    print(f"\n*** Affine Cipher ***")
    
    print("\n>>>  Encrypt <<<")
    result = encrypt(plainText, keyM, keyB)
    print(result["plainText"], len(result["plainText"]))
    print(result["keyM"])
    print(result["keyB"])
    print(result["cipherText"], len(result["cipherText"]))
    print(result["arrangedCipherText"], len(result["arrangedCipherText"]))

    print("\n>>>  Decrypt <<<")
    result = decrypt(result["cipherText"], keyM, keyB)
    print(result["cipherText"], len(result["cipherText"]))
    print(result["keyM"])
    print(result["keyB"])
    print(result["plainText"], len(result["plainText"]), "\n")