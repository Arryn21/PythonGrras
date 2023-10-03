# IPv4 address conversion into binary > four 8-bit octets

IP = input("Enter IP address in this format (255.255.255.255): ")
ip1 = IP.split(".")
ip2 = []
final = ""
ch = 0


for i in range(len(ip1)):
    ip2.append(int(ip1[i]))


for i in range(len(ip2)):
    if ip2[i] >= 128:
        final = final + "1"
        ip2[i] = ip2[i] - 128
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 64:
        final = final + "1"
        ip2[i] = ip2[i] - 64
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 32:
        final = final + "1"
        ip2[i] = ip2[i] - 32
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 16:
        final = final + "1"
        ip2[i] = ip2[i] - 16
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 8:
        final = final + "1"
        ip2[i] = ip2[i] - 8
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 4:
        final = final + "1"
        ip2[i] = ip2[i] - 4
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 2:
        final = final + "1"
        ip2[i] = ip2[i] - 2
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ip2[i] >= 1:
        final = final + "1"
        ip2[i] = ip2[i] - 1
        ch += 1
    else:
        final = final + "0"
        ch += 1
    if ch < 35:
        final = final + "."
        ch += 1

print(final)
