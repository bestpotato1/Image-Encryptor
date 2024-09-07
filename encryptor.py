from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import argparse
import os

def main():
    
    # creating parser
    parser = argparse.ArgumentParser(description="Parsing args for encryptor")
    parser.add_argument('-i', '--input', type=str, help="Input filename", required=True)
    parser.add_argument('-o', '--output', type=str, help="Output filename", required=True)
    parser.add_argument('-k', '--key', type=str, help="Key", required=True)
    parser.add_argument('-m', '--mode', type=str, help="Encryption mode", required=True)

    args = parser.parse_args()

    # opening Tux
    if args.input == "Tux.jpg":
        og_image = Image.open('Tux.jpg')
    elif args.input == "whoisCB2.jpg":
        og_image = Image.open('whoisCB2.jpg')

    # turning Tux to bytes
    img_bytes = og_image.tobytes()

    # generating key
    key = args.key.encode('utf-8')
    # iv for cbc algorithm
    iv = os.urandom(AES.block_size)
    
    if args.mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    elif args.mode == "CBC":
        cipher = AES.new(key, AES.MODE_CBC, iv)

    # pad the bytes and then encrypt them with the algorithm
    padded_bytes = pad(img_bytes, AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_bytes)

    # retrieve image size
    width, height = og_image.size

    # change frombytes()
    new_image = Image.frombytes(og_image.mode, (width, height), encrypted_bytes)

    # show the image
    new_image.save(args.output)
    new_image.show()
    new_image.close()

if __name__ == "__main__":
    main()