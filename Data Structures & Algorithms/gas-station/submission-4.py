class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netGas = [gas[i] - cost[i] for i in range(len(gas))]
        # [-1, 0, -1, 3]
        if sum(netGas) < 0: return -1
        total = 0
        maxTotal = 0
        res = 0
        for i, net in enumerate(netGas):
            total += net
            if total < 0:
                total = 0
                res = i + 1
        return res