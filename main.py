import DM_Cache as DM_Cache
import SA4_Cache as SA4_Cache
from ExtractData import results, fileNames
from tabulate import tabulate


print("Calculating values for Direct Mapped Cache....")
DM_Cache.calculateRates(results)
print("Direct Mapped Cache values are as follows:")
DM_array = []
for i in range(5):
    DM_array.append([fileNames[i], len(results[i]), DM_Cache.numHits[i], DM_Cache.numMisses[i], DM_Cache.numHits[i] /
                     len(results[i]), DM_Cache.numMisses[i]/len(results[i]), DM_Cache.numHits[i]/DM_Cache.numMisses[i]])

DM_table = tabulate(DM_array, headers=['File Name', 'Total Instructions', 'Hit Count', 'Miss Count',
                                       'Hit Rate', 'Miss Rate', 'Hit-Miss Ratio'], tablefmt='orgtbl')
print(DM_table)
print()


print("Calculating values for 4-Way Set Associative Cache....")
SA4_Cache.calculateRates(results)
SA4_array = []
print("4-way Set Associative Cache values are as follows:")
for i in range(5):
    SA4_array.append([fileNames[i], len(results[i]), SA4_Cache.numHits[i], SA4_Cache.numMisses[i], SA4_Cache.numHits[i] /
                      len(results[i]), SA4_Cache.numMisses[i]/len(results[i]), SA4_Cache.numHits[i]/SA4_Cache.numMisses[i]])

SA4_table = tabulate(SA4_array, headers=['File Name', 'Total Instructions', 'Hit Count', 'Miss Count',
                                         'Hit Rate', 'Miss Rate', 'Hit-Miss Ratio'], tablefmt='orgtbl')
print(SA4_table)
