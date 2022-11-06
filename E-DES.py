import hashlib
import random
import string

'''
def generate_key():
    N = 64
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return str(res)
print("key" + generate_key())
'''

key = "I don't show ID at clubs, 'cause they know that I am 21 - Savage"

def hash_sha256():
    hashed_key = hashlib.sha256(key.encode('utf-8')).hexdigest()
    return hashed_key

print(hash_sha256())