# Prasunet CS 02 - Image Encryption

<p align="center">
<a href="https://twitter.com/sbvignesh"><img src="https://img.shields.io/twitter/follow/sbvignesh.svg?logo=x"></a>
<a href="https://github.com/vigneshsb403/Prasunet_CS_02/pulls"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>

</p>

<p align="center">
  <a href="#installation">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#demo">Demo</a>
</p>

# Installation

### Requirements

 * Python
 * numpy

## Steps

clone the repo
```
git clone https://github.com/vigneshsb403/Prasunet_CS_02.git
```
Change directory
```
cd Prasunet_CS_02
```
Install the python modules
```
pip3 install -r requirements.txt
```

# Usage

```yaml
python3 main.py -h

    ______  _________                         __
   /  _/  |/  / ____/  ____________  ______  / /_
   / // /|_/ / / __   / ___/ ___/ / / / __ \/ __/
 _/ // /  / / /_/ /  / /__/ /  / /_/ / /_/ / /_
/___/_/  /_/\____/   \___/_/   \__, / .___/\__/
                              /____/_/
                        by: @sbvignesh
    
usage: main.py [-h] --input INPUT [--key_size KEY_SIZE] --mode {encrypt,decrypt} --output OUTPUT

Image encryption and decryption

options:
  -h, --help            show this help message and exit
  --input INPUT         Input image path
  --key_size KEY_SIZE   Size of the key (width and height of image)
  --mode {encrypt,decrypt}
                        Action to perform: 'encrypt' or 'decrypt'
  --output OUTPUT       Output image path
  ```

  # Demo

### Encryption:
```
python3 main.py --input file.jpg --mode encrypt --output enc_file.jpg
```
### Decryption:
```
python3 main.py --input enc_file.jpg --mode decrypt --output dec_file.jpg
```

---
Made with 🩵 by [@sbvignesh](https://twitter.com/sbvignesh)
