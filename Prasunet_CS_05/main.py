import argparse
import logging
from scapy.all import sniff
import time

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def banner():
    print("""
   _____ _   ____________________________ 
  / ___// | / /  _/ ____/ ____/ ____/ __ \\
  \\__ \\/  |/ // // /_  / /_  / __/ / /_/ /
 ___/ / /|  // // __/ / __/ / /___/ _, _/ 
/____/_/ |_/___/_/   /_/   /_____/_/ |_|  
                by: @sbvignesh                                          
          """)

def packet_handler(packet, verbose, output_file):
    global packet_count
    packet_count += 1
    
    output = []
    output.append("---------------------------------------")
    output.append(f"Packet Count: {packet_count}")
    output.append(f"Received at {time.ctime(packet.time)}")
    output.append(f"Packet Summary: {packet.summary()}")
    output.append(f"Packet Length: {len(packet)} bytes")

    if verbose:
        try:
            output.append("Packet Details:")
            output.append(str(packet))
        except Exception as e:
            output.append(f"Could not display packet details: {e}")
    
    output.append("Payload:")
    payload = bytes(packet)
    payload_str = ''
    for i in range(len(payload)):
        if payload[i] >= 32 and payload[i] < 127: # Printable characters
            payload_str += chr(payload[i])
            #output.append(chr(payload[i]))
        else:
            payload_str += '.'
            #output.append('.')
        if (i % 32 == 0 and i != 0) or (i == len(payload) - 1):
            output.append("")
    output.append(payload_str)
    output.append("Hex Dump:")
    hex_str = ' '.join(f'{b:02x}' for b in payload)
    output.append(hex_str)
    output.append("---------------------------------------\n")

    if output_file:
        with open(output_file, 'a') as f:
            f.write('\n'.join(output) + '\n')

    for line in output:
        print(line)

def main():
    banner()
    parser = argparse.ArgumentParser(description='Sniff network packets.')
    parser.add_argument('-i', '--interface', required=True, help='Network interface to sniff on')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-o', '--output', help='Output file to save packet details')
    parser.add_argument('-p', '--port', type=int, help='Port to filter on (optional)', required=False)

    args = parser.parse_args()

    global packet_count
    packet_count = 0
    print(f"Opening device {args.interface} for sniffing...")
    if args.port:
        filter_str = f"port {args.port}"
        print(f"Filtering on port {args.port}")
    else:
        filter_str = ""
    sniff(iface=args.interface, prn=lambda packet: packet_handler(packet, args.verbose, args.output), filter=filter_str)

if __name__ == "__main__":
    main()

