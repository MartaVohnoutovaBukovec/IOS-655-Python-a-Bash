# ch12_02.py
# hexadecimal

from codecs import encode, decode

# declare hex data
num = 0x64
print(num, '-->', chr(num))
num_s = "\x64"
print(num_s)

# display hex from string data
s = 'Hello world from Python'
s_bytes = s.encode()
s_hex = encode(s_bytes,'hex')
s_decoded = decode(s_hex, 'hex')
s_plaintext = s_decoded.decode()

print('plaintext:', s)
print('hex:', s_hex)
print('decoded:', s_plaintext)

# samples for displaying hex data
print('display hex format')
for c in s:
    print(c,'-->', encode(c.encode(),'hex'))


hex2 = ":".join("{:02x}".format(c) for c in s_bytes)
print(hex2)





