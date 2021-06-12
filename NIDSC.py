from functools import reduce
from random import randint

import numpy as np
import operator as op


def generateMemory(DRAM):
    for i in range(0, len(DRAM[0])):
        DRAM[i] = np.random.randint(0, 2, len(DRAM[0]))
        DRAM[i][reduce(op.xor, [i for i, bit in enumerate(DRAM[i]) if bit])] = not DRAM[i][
            reduce(op.xor, [i for i, bit in enumerate(DRAM[i]) if bit])]
    return DRAM.transpose()


def checkHammingCodes(hammingBlock):
    hammingBlock[reduce(op.xor, [i for i, bit in enumerate(hammingBlock) if bit])] = not hammingBlock[
        reduce(op.xor, [i for i, bit in enumerate(hammingBlock) if bit])]
    return hammingBlock


def rowHammer(DRAM, row):
    print(row)
    print(DRAM)
    for i in range(0, len(DRAM[row])):
        if randint(1, 2) == 1:
            DRAM[row][i] = not DRAM[row][i]
    print(DRAM)
    print("\n")


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
                rowHammer(DRAM, row + 1)  # zmiana

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
    return test


def main():
    howMuchBits = 16
    DRAM = np.zeros((howMuchBits, howMuchBits))
    DRAM = generateMemory(DRAM)

    DRAM = testMemory(DRAM)
    print(DRAM)


if __name__ == "__main__":
    main()
