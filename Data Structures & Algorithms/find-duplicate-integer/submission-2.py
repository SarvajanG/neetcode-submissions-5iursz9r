class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        index = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            index += 1
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow2
        return slow2 