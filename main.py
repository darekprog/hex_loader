
from io import StringIO

from intelhex import IntelHex
import numpy as np


ih = IntelHex('IPA.hex') # create empty object
pydict = ih.todict()     # dump contents to pydict
bin_array = ih.tobinarray()     # dump contents to pydict

# print(pydict)


sio = StringIO()
ih.write_hex_file(sio)
hexstr = sio.getvalue()
sio.close()

# print(hexstr)

print(bin_array)

# for elem in bin_array:
#     print("{:02X}".format(elem))

print(pydict)

# for  key, elem in pydict.items():
#     print("{:02X}".format(elem))
