s = b'Burning \'em, if you ain\'t quick and nimble'
s2 = b'I go crazy when I hear a cymbal'

key = b'ICE'
res = ''
res2 = ''

for i in range(len(s)):
    res += chr(s[i] ^ key[i%len(key)])

for i in range(len(s2)):
    res2 += chr(s2[i] ^ key[i%len(key)])


target = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272'
target2 = 'a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

target = bytearray.fromhex(target)
for x,y in zip(target,key):
    print(chr(x^y),end='')

