import re

def formatText(plainText: str) -> str:
    formatText = re.sub(r'[^\w]', ' ', plainText)
    formatText = re.sub(r'\_', ' ', formatText)
    formatText = re.sub(r'\d', ' ', formatText)
    formatText = formatText.replace(' ', '')
    
    return formatText.upper()

def arrangeText(cipherText: str) -> str:
    arrangedText = ""
    i = 0

    for letter in cipherText:
        i += 1
        arrangedText += letter
        if i == 5:
            arrangedText += " "
            i = 0
    
    return arrangedText

def charToInt(c: str) -> int:
    return ord(c) - ord('A')

def intToChar(i: int) -> str:
    return chr(i + ord('A'))
  
def shiftAlphabet(currentChar: str, shiftChar: str, mode: str):
    if mode == '+':
      return intToChar((charToInt(currentChar) + charToInt(shiftChar)) % 26)
    if mode == '-':
      return intToChar((charToInt(currentChar) - charToInt(shiftChar)) % 26)

def writeText(cipherText: str, destFile: str):
    with open(destFile, "w") as file:
        file.write(cipherText)
        file.close()

