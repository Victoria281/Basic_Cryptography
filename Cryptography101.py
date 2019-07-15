
def shift_right(text):    
    return (text[-1] + text[:-1])

def shift_left(text):    
    return (text[1:] + text[0])


def cryencrypt (plaintext, key):
    mid = (len(plaintext)-key)
    return (plaintext[mid:] + plaintext[:mid])

def crydecrypt (ciphertext, key):
    return (ciphertext[key:] + ciphertext[:key])




def create_key (codeword):
    result = []
    for i in codeword:
        result += [alpha.find(i.upper())+1]

    return result
    
def encrypt (plaintext, key):
    counter = 0
    plaintext = plaintext.upper()
    length = len(plaintext)
    for i in plaintext:
        if i.isspace():
            plaintext += " "
            
        else:
            increase = key[counter % 5]
            newindex = alpha.find(i) + increase

            while newindex >= len(alpha)-1:
                newindex = newindex -  len(alpha)

            plaintext += alpha[newindex]
            counter += 1
            
    return plaintext[length:]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt (ciphertext, codeword):

    result = []
    for i in codeword:
        result += [alpha.find(i.upper())+1]

    counter = 0
    length = len(ciphertext)
    ciphertext = ciphertext.upper()
    for i in ciphertext:
        if i.isspace():
            ciphertext += " "
            
        else:
            increase = result[counter % 5]
            newindex = alpha.find(i) - increase

            while newindex < 0:
                newindex = len(alpha) + newindex

            ciphertext += alpha[newindex]
            counter += 1
            
    return ciphertext[length:]

