# Prasunet CS 01 - Caesar Cipher

<p align="center">
<a href="https://twitter.com/sbvignesh"><img src="https://img.shields.io/twitter/follow/sbvignesh.svg?logo=x"></a>
<a href="https://github.com/vigneshsb403/Prasunet_CS_01"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>

</p>

<p align="center">
  <a href="#installation">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#demo">Demo</a>
</p>

# Installation

### Requirements

 * Python

## Steps

clone the repo
```
git clone https://github.com/vigneshsb403/Prasunet_CS_01.git
```
Change directory
```
cd Prasunet_CS_01
```

# Usage
```bash
python3 main.py -h
```
This will display help for the tool. Here are all the switches it supports.
```yaml

   ______                             _______       __
  / ____/__  ____ _________  _____   / ____(_)___  / /_  ___  _____
 / /   / _ \/ __ `/ ___/ _ \/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/  __/ /_/ (__  )  __/ /     / /___/ / /_/ / / / /  __/ /
\____/\___/\__,_/____/\___/_/      \____/_/ .___/_/ /_/\___/_/
                                         /_/  v.1.0
                                         by @sbvignesh

usage: main.py [-h] {encode,decode} text shift

Caesar Cipher encoder/decoder

positional arguments:
  {encode,decode}  Specify whether to encode or decode
  text             Text to be encoded or decoded
  shift            Shift value for the Caesar Cipher

options:
  -h, --help       show this help message and exit
```

# Demo

### Encode
```
python3 main.py encode "Test string" 2
```
result
```
   ______                             _______       __
  / ____/__  ____ _________  _____   / ____(_)___  / /_  ___  _____
 / /   / _ \/ __ `/ ___/ _ \/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/  __/ /_/ (__  )  __/ /     / /___/ / /_/ / / / /  __/ /
\____/\___/\__,_/____/\___/_/      \____/_/ .___/_/ /_/\___/_/
                                         /_/  v.1.0
                                         by @sbvignesh

Encoded text: Vguv uvtkpi
```

### Decode
```
python3 main.py decode "Vguv uvtkpi" 2
```
result
```

   ______                             _______       __
  / ____/__  ____ _________  _____   / ____(_)___  / /_  ___  _____
 / /   / _ \/ __ `/ ___/ _ \/ ___/  / /   / / __ \/ __ \/ _ \/ ___/
/ /___/  __/ /_/ (__  )  __/ /     / /___/ / /_/ / / / /  __/ /
\____/\___/\__,_/____/\___/_/      \____/_/ .___/_/ /_/\___/_/
                                         /_/  v.1.0
                                         by @sbvignesh

Decoded text: Test string
```


---
Made with 🩵 by [@sbvignesh](https://twitter.com/sbvignesh)

