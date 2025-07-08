from typing import List


def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    for start in range(len(gas)):
        curr_fuel = gas[start]
        end = start + n
        curr_ind = start
        while curr_ind < end:
            suff_fuel = cost[curr_ind % n]
            print(curr_ind, curr_fuel, suff_fuel)
            if curr_fuel < suff_fuel:
                break
            curr_fuel = curr_fuel - suff_fuel + gas[(curr_ind + 1) % n]
            curr_ind += 1

        if curr_ind == end:
            return start
    return -1
