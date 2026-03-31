class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        for (const auto& c : s) {
            sMap[c] += 1;
        }

        for (const auto& c : t) {
            tMap[c] += 1;
        }

        return sMap == tMap;
    }
};
