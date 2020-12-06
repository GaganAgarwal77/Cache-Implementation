# direct mapped cache of size 256kilobytes. Block size: 4 bytes. Assume a 32 bit address.
# Size =  64 * 4 *  2^10
# no.of lines = 64*2^10 = 2^16 = 65536
# index = 16 bits,  tag = 16 bits


numMisses = []  # stores the values of number of misses for the 5 trace files
numHits = []  # stores the values of number of hits for the 5 trace files


def calculateRates(results):
    for instructions in results:
        cache = [""]*pow(2, 16)  # cache with 2^16 lines
        missCount = 0
        # variables to count number of misses and hits
        hitCount = 0
        for instruction in instructions:
            # converting the hex address into binary
            binary = "{0:032b}".format(int(instruction, 0))
            tag = binary[0:14]  # first 14 bits are tag
            # index is the next 16 bits, we convert it into int for indexing
            index = int(binary[14:30], 2)
            # byte offset will be of two bits binary[31:32] as block size is 4 bytes
            # if the position in the cache is empty or holds a different tag we report a miss
            if(cache[index] == "" or cache[index] != tag):
                cache[index] = tag
                missCount += 1
            else:  # if the cache holds the tag we report a hit
                hitCount += 1

        numMisses.append(missCount)
        # finally adding the misses and hits to the arrays
        numHits.append(hitCount)
