#we are asked to write an xor function

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'

s1 = bytearray.fromhex(s1)
s2 = bytearray.fromhex(s2)

target = '746865206b696420646f6e277420706c6179'

sol = bytearray()
for x,y in zip(s1,s2):
    sol.append(x^y)
sol = sol.hex()
assert sol == target
