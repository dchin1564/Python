import itertools
import operator 
from itertools import chain
main_list = []
cycle_list = []
tuplevalues =((1, 10, 5, 2), (8, 48, 14, 63), (59, 47, 49, 22), (19, 60, 1, 40))

cycler = itertools.cycle(tuplevalues[0])
for i in range(0,len(tuplevalues[0]-1)):
    cycle_list.append(next(cycler))
main_list.append(tuple(cycle_list))

repeater = tuple(itertools.repeat(tuplevalues[1][0],4))
main_list.append(repeater)

accumulator = tuple(itertools.accumulate(tuplevalues[2],operator.add))
main_list.append(accumulator)

chain_list = []
j = 1

while j <= len(tuplevalues):
    chain_list.append(tuple(itertools.chain(tuplevalues[j-1])))
    j += 1 

new_list = list(chain.from_iterable(chain_list))


new_tuple = tuple(new_list)

main_list.append(new_tuple)

oddNum = list(itertools.filterfalse(lambda x : x % 2 == 0,new_tuple))

tup_oddNum = tuple(oddNum)

main_list.append(tup_oddNum)

main_tup = tuple(main_list)
print(main_tup)





