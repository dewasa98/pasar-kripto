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
        if p in key:
            ciphertext += key[p]
        else:
            if p == ' ':
                ciphertext += c
            else:
                ciphertext += '-'

    # again, we expect no error
    return ciphertext


def decrypt(ciphertext, key):
    # duplicated from encrypt :v
    # please be aware that the key used in decrypt is way in encrypt
    plaintext = ""

    for c in ciphertext:
        if c in key:
            plaintext += key[c]
        else:
            if c == ' ':
                plaintext += c
            else:
                plaintext += '-'

    return plaintext
