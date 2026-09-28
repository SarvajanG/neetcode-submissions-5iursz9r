class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(t)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1*num2)
                elif t == "/":
                    stack.append(int(num1/num2))
        return int(stack[-1])