class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed.sort(reverse=True)
        print(posSpeed)
        stack = []
        for item in posSpeed:
            if stack:
                topTime = (target - stack[-1][0])/stack[-1][1]
                curTime = (target - item[0])/item[1] 
                if curTime > topTime: # This car would not reach dest faster then car infront
                    stack.append(item)
            else:
                stack.append(item)
        return len(stack)