class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netGas = []
        for i in range(len(gas)):
            netGas.append(gas[i] - cost[i])

        # maxNetGas = max(netGas)
        # startIndex = netGas.index(maxNetGas)

        # [-1, 0, -1, 3]
        # [-1, 3, -4, 2]
        # total = netGas[startIndex]
        # i = (startIndex + 1) % len(gas)
        # while i % len(gas) != startIndex:
        #     total += netGas[i % len(gas)]
        #     if total < 0: 
        #         return -1
        #     i += 1
        if sum(netGas) < 0:
            return -1
        total = 0
        res = 0
        for i, net in enumerate(netGas):
            total += net
            if total < 0:
                total = 0
                res = i + 1

        return res
        
            