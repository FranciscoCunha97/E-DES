import hashlib
from random import *
import string

'''
def generate_key():
    N = 64
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return str(res)
print("key" + generate_key())
'''

def hash_sha256():
    hashed_key = hashlib.sha256(key.encode('utf-8')).hexdigest()
    return hashed_key

key = "I don't show ID at clubs, 'cause they know that I am 21 - Savage"

def rc4():
    hashed_key = hash_sha256()
    S = [x for x in range(256)]
    shuffle(S)
    j=0
    hashed_key=[ord(x) for x in hashed_key]
    for i in range(256):
        j = (j + S[i] + int(hashed_key[i % len(hashed_key)])) % 256
    
    """"
    for S_hex in
        h = []
        S_hex = hex(S_hex)
        h.append(S_hex)
    #print(len(S))
    """
    
    return S_hex

print(rc4())

