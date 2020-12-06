# 4-way set associative cache of size 256kilobytes. Block size: 4 bytes. 32 bit address.
# Size = 256 * 2^10 = 4 * 4 * 16  * 2^10
# no. of lines = 16 * 2^10 =  2^14 = 16384
# index = 14 bits , tag = 18 bits


numMisses = []  # stores the values of number of misses for the 5 trace files
numHits = []  # stores the values of number of hits for the 5 trace files


def calculateRates(results):
    for instructions in results:
        # cache with 2^14 lines, each line is essentially a dictionary with a maximum of 4 tags
        cache = []
        for i in range(pow(2, 14)):
            cache.append({})
        missCount = 0
        # variables to count number of misses and hits
        hitCount = 0
        instructionCount = 0  # maintaining instruction count for implementing LRU, the instruction which was referenced earliest the one with least instruction count is replaced
        for instruction in instructions:
            # converting the hex address into binary
            binary = "{0:032b}".format(int(instruction[2:], 16))
            tag = binary[0:16]  # first 16 bits are tag
            # index is the next 14 bits, we convert it into int for indexing
            index = int(binary[16:30], 2)
            # byte offset will be of two bits binary[31:32] as block size is 4 bytes
            if(tag not in cache[index]):
                # if the dictionary holds less than 4 tags we add a tag-instruction count pair normally
                if(len(cache[index]) < 4):
                    cache[index][tag] = instructionCount
                else:  # otherwise we need to do LRU
                    # a variable to find out the tag with the least instruction count
                    min = pow(2, 30)
                    min_tag = ''  # holds the tag with minimum instruction count we get
                    for i in cache[index]:
                        # going through the 4 tags in the dictionary to find the one with the least instruction count
                        if(cache[index][i] <= min):
                            min = cache[index][i]
                            min_tag = i
                    # deleting the tag-instruction count pair from the dictionary
                    del cache[index][min_tag]
                    # adding the new tag-instruction count pair
                    cache[index][tag] = instructionCount
                missCount += 1
            else:
                # updating the value of instruction count when it is a hit
                cache[index][tag] = instructionCount
                hitCount += 1
            instructionCount += 1
        numMisses.append(missCount)
        # finally adding the misses and hits to the arrays
        numHits.append(hitCount)
