def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Por favor, ingresa un mensaje para encriptar: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Por favor, ingresa una clave (un número entero del 1 al 25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        if currentCharacter in alphabet:
            newPosition = position + int(cipherKey)
            encryptedMessage += alphabet[newPosition]
        else:
            encryptedMessage += currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"Alfabeto: {myAlphabet}")
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f"Alfabeto duplicado: {myAlphabet2}")
    myMessage = getMessage()
    myCipherKey = getCipherKey()
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f"Mensaje encriptado: {myEncryptedMessage}")
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f"Mensaje desencriptado: {myDecryptedMessage}")

# Ejecutar el programa
runCaesarCipherProgram()
