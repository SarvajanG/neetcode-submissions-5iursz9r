class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill - 5 == 0: #gives 5
                five += 1
            elif bill - 5 == 5: #gives 10
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill - 5 == 15: #gives 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        return True