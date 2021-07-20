from io import StringIO

from intelhex import IntelHex
import numpy as np

hex_format_string = '02X'
bin_format_string = '08b'

ih = IntelHex('IPA.hex') # create empty object

# sio = StringIO()
# ih.write_hex_file(sio)
# hexstr = sio.getvalue()
# sio.close()
# print(hexstr)

bin_array = ih.tobinarray()     # dump contents to pydict
# print(bin_array)
# print(''.join([format(elem, '02X') for elem in bin_array]))

pydict = ih.todict()     # dump contents to pydict
# print(pydict)
start_address = pydict.pop('start_addr')
print(''.join([format(elem, hex_format_string) for elem in pydict.values()]))
# print(''.join([format(elem, bin_format_string) for elem in pydict.values()]))
print(start_address)