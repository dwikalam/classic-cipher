import string

# import sys
# sys.path.append("../src")
import utilities

CHARSET = string.ascii_uppercase
ROTOR_I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'  
ROTOR_II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'  
ROTOR_III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'  
REFLECTOR = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'  

def encrypt(plainText, key1, key2, key3, encrypt = True):
    key1 = key1[:1].upper()
    key2 = key2[:1].upper()
    key3 = key3[:1].upper()
    ROTOR_OFFSET_I = CHARSET.index(key1)
    ROTOR_OFFSET_II = CHARSET.index(key2)
    ROTOR_OFFSET_III = CHARSET.index(key3)
    ROTOR_SHIFT_I = [(ord(ROTOR_I[i]) - ord(CHARSET[i])) % 26 for i in range(26)]
    ROTOR_SHIFT_II = [(ord(ROTOR_II[i]) - ord(CHARSET[i])) % 26 for i in range(26)]
    ROTOR_SHIFT_III = [(ord(ROTOR_III[i]) - ord(CHARSET[i])) % 26 for i in range(26)]
    REFLECTOR_SHIFT = [(ord(REFLECTOR[i]) - ord(CHARSET[i])) % 26 for i in range(26)]
    plainText = ''.join(filter(str.isalpha, plainText.upper())) 
    cipherText = ''

    for char in plainText:
        imm_idx = CHARSET.index(char)
        
        ROTOR_OFFSET_III = (ROTOR_OFFSET_III + 1) % 26
        if ROTOR_OFFSET_III == 0: 
            ROTOR_OFFSET_II = (ROTOR_OFFSET_II + 1) % 26
            if ROTOR_OFFSET_II == 0: 
                ROTOR_OFFSET_I = (ROTOR_OFFSET_I + 1) % 26

        imm_idx = (imm_idx + ROTOR_SHIFT_III[(imm_idx + ROTOR_OFFSET_III) % 26]) % 26
        imm_idx = (imm_idx + ROTOR_SHIFT_II[(imm_idx + ROTOR_OFFSET_II) % 26]) % 26
        imm_idx = (imm_idx + ROTOR_SHIFT_I[(imm_idx + ROTOR_OFFSET_I) % 26]) % 26

        imm_idx = (imm_idx + REFLECTOR_SHIFT[(imm_idx) % 26]) % 26

        l_inp_idx = (imm_idx + ROTOR_OFFSET_I) % 26
        imm_pair_idx = ROTOR_I.index(CHARSET[l_inp_idx])
        imm_idx = (imm_idx - ROTOR_SHIFT_I[imm_pair_idx]) % 26
        l_inp_idx = (imm_idx + ROTOR_OFFSET_II) % 26
        imm_pair_idx = ROTOR_II.index(CHARSET[l_inp_idx])
        imm_idx = (imm_idx - ROTOR_SHIFT_II[imm_pair_idx]) % 26
        l_inp_idx = (imm_idx + ROTOR_OFFSET_III) % 26
        imm_pair_idx = ROTOR_III.index(CHARSET[l_inp_idx])
        imm_idx = (imm_idx - ROTOR_SHIFT_III[imm_pair_idx]) % 26

        cipherText += CHARSET[imm_idx]

    result = {
        "plainText": plainText,
        "key1": key1,
        "key2": key2,
        "key3": key3,
        "cipherText": cipherText,
        "arrangedCipherText": utilities.arrangeText(cipherText)
    }

    if (encrypt): 
        utilities.writeText(cipherText, "../data/output/enigma-cipher.txt")
        
    return result

def decrypt(cipherText, key1, key2, key3):
    result = encrypt(cipherText, key1, key2, key3, encrypt=False)

    temp = result["plainText"]
    result["plainText"] = result["cipherText"]
    result["cipherText"] = temp

    return result

if __name__ == "__main__":
    plainText = input("> Plain text: ")
    key1 = input("> Key 1: ")
    key2 = input("> Key 2: ")
    key3 = input("> Key 3: ")

    # Enigma Cipher
    print(f"\n*** Enigma Cipher ***")
    print("\n>>>  Encrypt <<<")
    result = encrypt(plainText, key1, key2, key3)
    print(result["plainText"], len(result["plainText"]))
    print(result["key1"])
    print(result["key2"])
    print(result["key3"])
    print(result["cipherText"], len(result["cipherText"]))
    print(result["arrangedCipherText"], len(result["arrangedCipherText"]))

    print("\n>>>  Decrypt <<<")
    result = decrypt(plainText, key1, key2, key3)
    print(result["cipherText"], len(result["cipherText"]))
    print(result["key1"])
    print(result["key2"])
    print(result["key3"])
    print(result["plainText"], len(result["plainText"]))