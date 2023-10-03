# conversion code from ChatGPT

def validate_ipv4(ip):
    octets = ip.split(".")
    if len(octets) == 4:
        for octet in octets:
            if not octet.isdigit() or not (0 <= int(octet) <= 255):
                return False
        return True
    return False


def convert_to_binary(ip):
    binary_ip = ""
    octets = ip.split(".")
    for octet in octets:
        binary_ip += format(int(octet), '08b') + "."
    return binary_ip[:-1]  # Remove the trailing '.'


def main():
    IP = input("Enter IP address in this format (255.255.255.255): ")

    if validate_ipv4(IP):
        binary_ip = convert_to_binary(IP)
        print(f"The binary representation of {IP} is: {binary_ip}")
    else:
        print("Invalid IPv4 address format.")


if __name__ == "__main__":
    main()
