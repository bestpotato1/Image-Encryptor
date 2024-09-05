from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# opening Tux
og_image = Image.open('Tux.jpg')

# turning Tux to bytes
img_bytes = og_image.tobytes()

# generating key
key = b'00112233445566778889aabbccddeeff'
cipher = AES.new(key, AES.MODE_ECB)

# pad the bytes and then encrypt them with the algorithm
padded_bytes = pad(img_bytes, AES.block_size)
encrypted_bytes = cipher.encrypt(padded_bytes)

# retrieve image size
width, height = og_image.size

# change frombytes()
new_image = Image.frombytes(og_image.mode, (width, height), encrypted_bytes)

# show the image
new_image.save("tux_modded.jpg")
new_image.show()
