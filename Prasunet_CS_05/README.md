# Prasunet CS 05 - Network Packet Analyzer

<p align="center">
<a href="https://twitter.com/sbvignesh"><img src="https://img.shields.io/twitter/follow/sbvignesh.svg?logo=x"></a>
<a href="https://github.com/vigneshsb403/Prasunet_CS_03/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>

</p>

<p align="center">
  <a href="#installation">Install</a> •
  <a href="#usage">Usage</a> •
  <a href="#demo">Demo</a>
</p>

# Installation

### Requirements

 * Python
 * scapy

## Steps

clone the repo
```
https://github.com/vigneshsb403/Prasunet_CS_05.git
```
Change directory
```
cd Prasunet_CS_05
```

# Usage
```bash
python3 main.py -h
```
This will display help for the tool.
```yaml

   _____ _   ____________________________ 
  / ___// | / /  _/ ____/ ____/ ____/ __ \
  \__ \/  |/ // // /_  / /_  / __/ / /_/ /
 ___/ / /|  // // __/ / __/ / /___/ _, _/ 
/____/_/ |_/___/_/   /_/   /_____/_/ |_|  
                by: @sbvignesh                                          
          
usage: main.py [-h] -i INTERFACE [-v] [-o OUTPUT] [-p PORT]

Sniff network packets.

options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Network interface to sniff on
  -v, --verbose         Enable verbose output
  -o OUTPUT, --output OUTPUT
                        Output file to save packet details
  -p PORT, --port PORT  Port to filter on (optional)
```

# Demo

```
sudo python3 main.py -i lo0

   _____ _   ____________________________ 
  / ___// | / /  _/ ____/ ____/ ____/ __ \
  \__ \/  |/ // // /_  / /_  / __/ / /_/ /
 ___/ / /|  // // __/ / __/ / /___/ _, _/ 
/____/_/ |_/___/_/   /_/   /_____/_/ |_|  
                by: @sbvignesh                                          
          
Opening device lo0 for sniffing...
---------------------------------------
Packet Count: 1
Received at Wed Jul 10 15:10:24 2024
Packet Summary: Loopback / IPv6 / TCP ::1:50519 > ::1:http PA / Raw
Packet Length: 148 bytes
Payload:





....`....h.@.................................W.PA..X.........p.............mGET / HTTP/1.1..Host: localhost..User-Agent: curl/8.7.1..Accept: */*....
Hex Dump:
1e 00 00 00 60 0a 09 00 00 68 06 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 c5 57 00 50 41 18 8e 58 1e 10 8e 0a 80 18 18 e3 00 70 00 00 01 01 08 0a 07 a6 f3 87 d6 e0 8f 6d 47 45 54 20 2f 20 48 54 54 50 2f 31 2e 31 0d 0a 48 6f 73 74 3a 20 6c 6f 63 61 6c 68 6f 73 74 0d 0a 55 73 65 72 2d 41 67 65 6e 74 3a 20 63 75 72 6c 2f 38 2e 37 2e 31 0d 0a 41 63 63 65 70 74 3a 20 2a 2f 2a 0d 0a 0d 0a
---------------------------------------


```

---
Made with 🩵 by [@sbvignesh](https://twitter.com/sbvignesh)
