class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed.sort(reverse=True)

        res = []
        for car in posSpeed:
            curTime = (target - car[0]) / car[1]
            if res:
                topTime = (target - res[-1][0]) / res[-1][1]
                if curTime > topTime:
                    res.append(car)
            else:
                res.append(car)
        return len(res)