## STR
import struct

from insoft.openmanager.message.packet import Packet

str_name = "kim dong min"
str_bin = bytes(str_name, "utf-8")
print("BIN : %s" % str_bin)
print("LENGTH : %d" % len(str_bin))
print("STR : %s" % str_bin.decode())
print("")


## INT
float_name = 4
float_bin = float_name.to_bytes(4, "big")

print("BIN : %s" % float_bin)
print("LENGTH : %d" % len(float_bin))
print("INT : %s" % int.from_bytes(float_bin, "big"))
print("")

test_bin = bytes(b'\x0b') # Server ID
print(len(test_bin))
print(int.from_bytes(test_bin, "big"))

test_bin = bytes(b'\x00') # Flag
print(len(test_bin))
print(int.from_bytes(test_bin, "big"))

test_bin = bytes(b'\x00\x04\x93\xec') # Request ID
print(len(test_bin))
print(int.from_bytes(test_bin, "big"))

# AGENT 6 BYTE

# LONG
## INT
float_name = 8
float_bin = float_name.to_bytes(8, "big")

print("BIN : %s" % float_bin)
print("LENGTH : %d" % len(float_bin))
print("LONG : %s" % int.from_bytes(float_bin, "big"))
print("")

# FLOAT
p = struct.pack('f', 3.141592654)

print(p, len(p), struct.unpack('f', p))

print(struct.unpack('!i', b'\x00\x00\x00\x06'))

print(struct.unpack_from('!I', bytes(b'\x0b\x00\x00\x04\x93\xec'), 2))



