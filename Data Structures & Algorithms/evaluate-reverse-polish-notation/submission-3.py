class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                sum = stack.pop() + stack.pop()
                stack.append(sum)
            elif t == "-":
                difference = (stack.pop() - stack.pop())*-1
                stack.append(difference)
            elif t == "*":
                product = stack.pop() * stack.pop()
                stack.append(product)
            elif t == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                quotient = int(num1 / num2)
                stack.append(quotient)
            else:
                stack.append(int(t))
            print(stack)
        return stack[-1]