def input_key(key_dict):
    # expecting string representation of dictionary
    # ie {'a':'b', 'b':'c', . . .}
    import ast

    # for now, we expect everything fit in, lol
    return ast.literal_eval(key_dict)


def encrypt(plaintext, key):
    # expecting plaintext of string
    # expecting key from input_key
    ciphertext = ""

    for p in plaintext:
        ciphertext += key[p]

    # again, we expect no error
    return ciphertext


def decrypt(message, key):
    # duplicated from encrypt :v
    # please be aware that the key used in decrypt is way in encrypt
    plaintext = ""
    
    for c in ciphertext:
        plaintext += key[c]

    return plaintext
