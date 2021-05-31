from functools import reduce
import numpy as np
import operator as op


bits=np.random.randint(0,2,16)

print(bits)

print(reduce(op.xor,[i for i, bit in enumerate(bits) if bit]))

bits[reduce(op.xor,[i for i, bit in enumerate(bits) if bit])]=not bits[reduce(op.xor,[i for i, bit in enumerate(bits) if bit])]

print(bits)

print(reduce(op.xor,[i for i, bit in enumerate(bits)]))