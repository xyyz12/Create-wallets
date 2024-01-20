import re

file_path = 'C:\\Users\\1\\Desktop\\111\\wallets.txt'
output_file_path = 'C:\\Users\\1\\Desktop\\111\\wallets1.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

    wallet_addresses = []
    for line in lines:
        match = re.search(r'地址:\s*(\w+)', line)
        if match:
            address = match.group(1)
            wallet_addresses.append(address)

with open(output_file_path, 'w') as output_file:
    for address in wallet_addresses:
        output_file.write(address + '\n')

print("Addresses saved to wallets1.txt")