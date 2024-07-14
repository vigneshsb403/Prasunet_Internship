from PIL import Image
import numpy as np
import argparse

def banner():
    print("""
    ______  _________                         __
   /  _/  |/  / ____/  ____________  ______  / /_
   / // /|_/ / / __   / ___/ ___/ / / / __ \\/ __/
 _/ // /  / / /_/ /  / /__/ /  / /_/ / /_/ / /_
/___/_/  /_/\\____/   \\___/_/   \\__, / .___/\\__/
                              /____/_/
                        by: @sbvignesh
    """)

def encrypt_image(input_image_path, output_image_path, key):
    img = Image.open(input_image_path)
    img = img.convert("RGB")
    img_array = np.array(img)
    encrypted_img_array = np.bitwise_xor(img_array, key)
    encrypted_img = Image.fromarray(encrypted_img_array.astype('uint8'), 'RGB')
    encrypted_img.save(output_image_path)
    print(f"[*INFO] Image encrypted successfully. Encrypted image saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    encrypted_img = Image.open(input_image_path)
    encrypted_img = encrypted_img.convert("RGB")
    encrypted_img_array = np.array(encrypted_img)
    decrypted_img_array = np.bitwise_xor(encrypted_img_array, key)
    decrypted_img = Image.fromarray(decrypted_img_array.astype('uint8'), 'RGB')
    decrypted_img.save(output_image_path)
    print(f"[*INFO] Image decrypted successfully. Decrypted image saved as {output_image_path}")

if __name__ == "__main__":
    banner()

    parser = argparse.ArgumentParser(description='Image encryption and decryption')
    parser.add_argument('--input', required=True, help='Input image path')
    parser.add_argument('--key_size', type=int, default=256, help='Size of the key (width and height of image)')
    parser.add_argument('--mode', choices=['encrypt', 'decrypt'], required=True, help="Action to perform: 'encrypt' or 'decrypt'")
    parser.add_argument('--output', required=True, help='Output image path')

    args = parser.parse_args()

    input_image_path = args.input
    mode = args.mode
    output_image_path = args.output
    key_size = args.key_size

    img = Image.open(input_image_path)
    width, height = img.size
    key = np.full(img_array.shape, 255, dtype=np.uint8)
    if mode == 'encrypt':
        encrypt_image(input_image_path, output_image_path, key)
    elif mode == 'decrypt':
        decrypt_image(input_image_path, output_image_path, key)
    else:
        print("[!]ERROR: Invalid 'mode', Please specify 'encrypt' or 'decrypt'.")
