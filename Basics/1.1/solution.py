import binascii
import base64
#we are asked to convert hex to base64

given = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
target = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

given = base64.b64encode(binascii.unhexlify(given)).decode()
assert given == target
