#!/usr/bin/env python3

import argparse

VERSION = "1.0"

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the text using the Caesar Cipher algorithm.
    
    Args:
    - text: The string to be encrypted or decrypted.
    - shift: The number of positions each letter in text should be shifted.
    - mode: 'encode' for encryption, 'decode' for decryption.
    
    Returns:
    - The encrypted or decrypted string.
    """
    result = []
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encode':
                shifted = (ord(char) - base + shift) % 26 + base
            elif mode == 'decode':
                shifted = (ord(char) - base - shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)  # Preserve non-alphabetic characters
    
    return ''.join(result)

def banner(version):
    string = f"""   
   ______                             _______       __             
  / ____/__  ____ _________  _____   / ____(_)___  / /_  ___  _____
 / /   / _ \\/ __ `/ ___/ _ \\/ ___/  / /   / / __ \\/ __ \\/ _ \\/ ___/
/ /___/  __/ /_/ (__  )  __/ /     / /___/ / /_/ / / / /  __/ /    
\\____/\\___/\\__,_/____/\\___/_/      \\____/_/ .___/_/ /_/\\___/_/     
                                         /_/  v.{version}
                                         by @sbvignesh
    """
    print(string)

def main():
    banner(VERSION)
    parser = argparse.ArgumentParser(description='Caesar Cipher encoder/decoder')
    parser.add_argument('mode', choices=['encode', 'decode'], help='Specify whether to encode or decode')
    parser.add_argument('text', type=str, help='Text to be encoded or decoded')
    parser.add_argument('shift', type=int, help='Shift value for the Caesar Cipher')

    try:
        args = parser.parse_args()

        if not 0 <= args.shift < 26:
            raise ValueError("Shift value must be between 0 and 25")

        if args.mode == 'encode':
            result = caesar_cipher(args.text, args.shift, mode='encode')
            print(f"Encoded text: {result}")
        elif args.mode == 'decode':
            result = caesar_cipher(args.text, args.shift, mode='decode')
            print(f"Decoded text: {result}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyboardInterrupt:
        print("\nOperation interrupted. Exiting gracefully...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

