from string import printable
with open('4.txt','r') as fp:
    lines = fp.readlines()

def discrim(s):
    for i in s:
        if i not in printable:
           return 
    print(s)


def strxor(s,a):
    text = ''
    for i in s:
        text += chr(i^ord(a))
    return text

for line in lines:
    tmp = bytearray.fromhex(line)
    for char in printable:
        discrim(strxor(tmp,char))


#using a discriminator to condense lines
#from output: `Now that the party is jumping`
