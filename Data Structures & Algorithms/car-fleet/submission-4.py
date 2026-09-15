class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)
        prevTime = (target - cars[0][0]) / cars[0][1]
        # print(position[0], speed[0]) 
        res = 1
        for pos, sp in cars[1:]:
            currTime = (target - pos) / sp
            # print(currTime, prevTime)
            if currTime > prevTime:
                prevTime = currTime
                res += 1

        return res