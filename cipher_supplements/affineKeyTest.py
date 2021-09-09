# Program to prove that keyspace of the affine cipher is limited to less
# than len(SYMBOLS)^2

import affineCipher
from cipher_supplements import cryptomath

message = "Make things as simple as possible, but not simpler."
for keyA in range(2, 80):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key, message))