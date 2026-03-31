class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numToIndex;
        for (int i; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numToIndex.contains(complement)) {
                return {numToIndex[complement], i};
            } else {
                numToIndex[nums[i]] = i;
            }
        }
        return {};
    }
};
