from functools import reduce
from random import randint

import numpy as np
import operator as op


def generateMemory(DRAM):
    for i in range(0, len(DRAM[0])):
        hammingBlock = np.random.randint(0, 2, len(DRAM[0]))
        hammingBlock = checkHammingCodes(hammingBlock)
        DRAM[:, i] = hammingBlock
    print("Memory checked, errors corrected")
    return DRAM


def checkHammingCodes(hammingBlock):
    if reduce(op.xor, [i for i, bit in enumerate(hammingBlock) if bit]) !=0:
        print("Problem found in lane:",reduce(op.xor, [i for i, bit in enumerate(hammingBlock) if bit]))
    hammingBlock[reduce(op.xor, [i for i, bit in enumerate(hammingBlock) if bit])] = not hammingBlock[
        reduce(op.xor, [i for i, bit in enumerate(hammingBlock) if bit])]
    if hammingBlock.sum() % 2:
        hammingBlock[0] = not hammingBlock[0]
    return hammingBlock


def rowHammer(DRAM, row):
    for i in range(0, len(DRAM[row])):
        if randint(1, 2) == 1:
            DRAM[row][i] = not DRAM[row][i]


def rowAccess(DRAM, row):
    rowData = DRAM[row]
    error = randint(1, 100)
    if error <= 2:
        if error == 2:
            if row >= len(DRAM[0]) - 1:
                rowHammer(DRAM, row - 1)
            else:
                rowHammer(DRAM, row + 1)
        else:
            if row <= 0:
                rowHammer(DRAM, row + 1)
            else:
                rowHammer(DRAM, row - 1)

    return rowData


def memoryAccess(DRAM, test):
    for i in range(0, (len(DRAM[0]))):
        test[i] = rowAccess(DRAM, i)


def testMemory(DRAM):
    test = np.zeros((len(DRAM[0]), len(DRAM[0])))
    memoryAccess(DRAM, test)
    for i in range(0, (len(DRAM[0]))):
        hammingBlock = test[:, i]
        test[:, i] = checkHammingCodes(hammingBlock)
    print("Memory checked, errors corrected")
    return test


def main():
    howMuchBits = 16
    DRAM = np.zeros((howMuchBits, howMuchBits))
    print("Generated memory")
    DRAM = generateMemory(DRAM)
    for i in range(0,20):
        DRAM = testMemory(DRAM)




if __name__ == "__main__":
    main()
