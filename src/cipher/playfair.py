import utilities

alphabets = [chr(65 + i) for i in range(26)]
KEYSIZE = 5

def encrypt(plainText: str, plainKey: str):
    formatText, matrix = preprocess(plainText, plainKey)
    i = 0
    formatTextLength = len(formatText)
    cipherText = ""

    while i < formatTextLength:
        if i + 1 < formatTextLength:
            if formatText[i] == formatText[i+1]:
                formatText = formatText[:i+1] + 'X' + formatText[i+1:]
                formatTextLength += 1
        else: 
            formatText += 'X'

        letter1, letter2 = encryptBigram(formatText[i], formatText[i + 1], matrix)
        cipherText += letter1 + letter2
        i += 2

    result = {
        "plainText": formatText,
        "cipherText": cipherText,
        "arrangedCipherText": utilities.arrangeText(cipherText)
    }

    utilities.writeText(cipherText, "../data/output/playfair-cipher.txt")
    return result

def decrypt(cipherText: str, key: str):
    formatCipherText, matrix = preprocess(cipherText, key)
    i = 0
    n = len(formatCipherText)
    decryptedText = ""

    while i < n:
        if i+1 < n:
            if formatCipherText[i] == formatCipherText[i+1]:
                formatCipherText = formatCipherText[:i+1] + 'X' + formatCipherText[i+1:]
                n += 1
        else:
            formatCipherText += 'X'
        letter1, letter2 = decryptBigram(formatCipherText[i], formatCipherText[i+1], matrix)
        decryptedText += letter1 + letter2
        i += 2

    result = {
        "cipherText": formatCipherText,
        "plainText": decryptedText
    }
    
    return result

def encryptBigram(p1, p2, matrix):
    i1, j1 = getIdx(matrix, p1)
    i2, j2 = getIdx(matrix, p2)

    if (i1 == i2):
        return matrix[i1][(j1 + 1) % KEYSIZE], matrix[i1][(j2 + 1) % KEYSIZE]
    elif j1 == j2:
        return matrix[(i1 + 1) % KEYSIZE][j1], matrix[(i2 + 1) % KEYSIZE][j1]
    
    return matrix[i1][j2], matrix[i2][j1]

def decryptBigram(p1, p2, matrix):
    i1, j1 = getIdx(matrix, p1)
    i2, j2 = getIdx(matrix, p2)

    if (i1 == i2):
        return matrix[i1][(j1 - 1) % KEYSIZE], matrix[i1][(j2 - 1) % KEYSIZE]
    elif j1 == j2:
        return matrix[(i1 - 1) % KEYSIZE][j1], matrix[(i2 - 1) % KEYSIZE][j1]
    
    return matrix[i1][j2], matrix[i2][j1]

def preprocess(plainText, plainKey):
    formatText = "".join(char for char in plainText if char not in ' ,.?!(){}-+_')
    formatKey = "".join(char for char in plainKey if char not in ' ,.?!(){}jJ')
    formatText = formatText.upper()
    formatText = formatText.replace('J', 'I')
    formatKey = formatKey.upper()
    newkey = ""

    for char in formatKey:
        if char not in newkey:
            newkey += char
    formatKey = newkey
    
    for char in alphabets:
        if char not in formatKey:
            formatKey += char
    matrix = [[formatKey[KEYSIZE * i + j] for j in range(KEYSIZE)] for i in range(KEYSIZE)]

    return formatText, matrix

def getIdx(matrix: list, letter: str):
    for row in range(KEYSIZE):
        for col in range(KEYSIZE):
            if matrix[row][col] == letter:
                return row, col
    return -1,-1

if __name__ == "__main__":
    plainText = input("> Plain text: ")
    plainKey = input("> Plain key: ")

    # Playfair Cipher
    print(f"\n*** Playfair Cipher ***")
    
    print("\n>>>  Encrypt <<<")
    result = encrypt(plainText, plainKey)
    print(result["plainText"], len(result["plainText"]))
    print(result["cipherText"], len(result["cipherText"]))
    print(result["arrangedCipherText"], len(result["arrangedCipherText"]))

    print("\n>>>  Decrypt <<<")
    result = decrypt(result["cipherText"], plainKey)
    print(result["cipherText"], len(result["cipherText"]))
    print(result["plainText"], len(result["plainText"]), "\n")