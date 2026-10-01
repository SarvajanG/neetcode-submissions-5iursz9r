class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        stack = []
        fleets = 0
        for i in range(len(position)):
            posSpeed.append((position[i],speed[i]))
        posSpeed.sort(reverse=True)
        #print(posSpeed)
        for pair in posSpeed:
            time = (target - pair[0])/pair[1]
            if stack and time > stack[0]:
                fleets += 1
                stack = []
            stack.append(time)
            #print(stack)
        if stack:
            fleets += 1
        
        #print(fleets)
        return fleets