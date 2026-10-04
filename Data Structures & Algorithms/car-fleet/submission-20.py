class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        stack = []
        for i in range(len(position)):
            posSpeed.append((position[i], speed[i]))

        posSpeed.sort(reverse=True)

        for pair in posSpeed:
            curTime = (target - pair[0])/pair[1]
            if stack:
                if curTime > stack[-1]:
                    stack.append(curTime)
            else:
                stack.append(curTime)
        return len(stack)