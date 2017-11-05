from struct import *

# store as bytes data
packed_data = pack('iif', 6, 9, 3.168)
print(packed_data)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('d'))

# unpack bytes data to original data
unpacked_data = unpack('iif', packed_data)
print(unpacked_data)
print(unpack('iif', b'\x06\x00\x00\x00\t\x00\x00\x00\x83\xc0J@'))