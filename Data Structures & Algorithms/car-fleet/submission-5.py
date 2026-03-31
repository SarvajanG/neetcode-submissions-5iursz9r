class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        posSpeed.sort(reverse=True)
        
        stack = []
        for item in posSpeed:
            curTime = (target - item[0])/item[1]
            if stack:
                lead = stack[-1]
                leadTime = (target - lead[0])/lead[1]
                if curTime > leadTime:
                    stack.append(item)
            else:
                stack.append(item)
        return len(stack)