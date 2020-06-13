from Crypto.Cipher import AES

key = b'YELLOW SUBMARINE'
with open('7.txt','r') as fp:
    lines = fp.readlines()

#because ecb we can decrypt line by line w/o joining


for line in lines:
    print(line,len(line))
    cipher = AES.new(key, AES.MODE_ECB)
    print(cipher.decrypt(line.encode()))

