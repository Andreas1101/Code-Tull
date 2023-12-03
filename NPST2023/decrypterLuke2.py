import codecs
from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

file_to_decrypt = 'huskeliste.txt.enc'
result_file = 'huskeliste.txt'

# The key should be the hexadecimal string provided by the ransom note
key_hex = "dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128"
key = binascii.unhexlify(key_hex)

# The IV will need to be the one originally used for encryption, after reversing any ROT13 transformation
iv = "UtgangsVektor123"  # Replace this with your actual IV

# Decode the IV with ROT13 if it was encoded
decoded_iv = codecs.encode(iv, 'rot-13')

# Use the Counter object for CTR mode, with the ROT13-decoded IV
ctr = Counter.new(128, initial_value=int.from_bytes(decoded_iv.encode('utf-8'), 'big'))

# Read the encrypted file
with open(file_to_decrypt, 'rb') as encrypted_file:  # Replace with your actual file path
    encrypted_data = encrypted_file.read()

# Decrypt the data
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
decrypted_data = cipher.decrypt(encrypted_data)

# Write the decrypted data to a file
with open(result_file, 'wb') as decrypted_file:  # Replace with your actual output file path
    decrypted_file.write(decrypted_data)

print('Decryption complete.')
