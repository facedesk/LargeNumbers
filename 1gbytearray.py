

number_of_bytes = 2
binary_in_ram= bytearray([1] * number_of_bytes)

byte = ord(binary_in_ram[0])
# now convert to string of 1s and 0s
byte = bin(byte)[2:].rjust(8, '0')
# now byte contains a string with 0s and 1s
for bit in byte:
    print(bit)


number_from_bytes = int.from_bytes(binary_in_ram, byteorder='big', signed=False)
print(number_from_bytes)