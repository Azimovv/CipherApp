# Caesar Cipher
from random import randint
from cipher_supplements.detectEnglish import isEnglish

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'


# Encryption function
def encryptor(message, key):
    crypted = ''

    for character in message:
        new_index = symbols.find(character) + key

        # Handling wraparound
        if new_index >= len(symbols):
            new_index = new_index - len(symbols)
        elif new_index < 0:
            new_index = new_index + len(symbols)

        crypted += symbols[new_index]

    return f" '{crypted}' with a key of {key}"


# Brute force decryption function
def decryptor(message):
    crypted = ''

    for i in range(len(symbols)):
        for character in message:
            new_index = symbols.find(character) - i
            if new_index < 0:
                new_index = new_index + len(symbols)
            crypted += symbols[new_index]
        if isEnglish(crypted):
            return f" '{crypted}', with key {i}"
        else:
            crypted = ''
    return 'Unable to decrypt, possible reasons: different symbol set used to ' \
           'encrypt than the one that is used in this program or the original phrase ' \
           'did not contain enough english words.'


# Handler for encryption and decryption functions
def crypter(message, key, encOrdec):

    # Brute force method for decryption
    if key == 0 and encOrdec == 3:
        return decryptor(message)

    # Encryption
    elif key == 0 and encOrdec == 1:
        # create random key if none is provided
        key = randint(1, len(symbols))
        return encryptor(message, key)


print(crypter('what up homie', 0, 3))