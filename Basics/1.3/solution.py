from string import printable
#we are given a hex encoded string and need to find the character it was xor'd with 

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
s = bytearray.fromhex(s)

def strxor(s,a):
    for i in s:
        print(chr(i ^ord(a)),end='')

for char in printable:
    strxor(s,char)
    print('')

#looking at the output: `Cooking MC's like a pound of bacon`

