class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        stack = []

        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])

        posSpeed.sort(reverse=True)

        for car in posSpeed:
            time = (target - car[0])/car[1]
            if stack:
                if time > stack[-1][1]:
                    stack.append([car[0], time])
            else:
                stack.append([car[0], time])
        return len(stack)