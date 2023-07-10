import random
import math
import os
#pip install sympy
from sympy import isprime

#decrypt files

def decrypt(input_file,private_key_str):
    private_key_parts = private_key_str.strip('()\n').split(',')
    print(private_key_parts)
    d = int(private_key_parts[0].strip())
    n = int(private_key_parts[1].strip())
    decryptmessage=""

    with open(input_file,'r') as file:
        encryptmessage = file.read().split(',')
    print(encryptmessage)

    for char in encryptmessage:
        charcontinue=pow(int(char),d,n)
        decryptmessage+=chr(charcontinue)

    with open(input_file,'w') as file:
        file.write(decryptmessage)
        print(decryptmessage)

# scan for files and store in files
files=[]
for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == "private_key.txt":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)


#decrypt every file call 

with open('private_key.txt', 'r') as private_file:
    private_key_str = private_file.read()

    

for input_file in files:
    dec_message=decrypt(input_file,private_key_str)
    print("decrypted_message : ",dec_message)




        
