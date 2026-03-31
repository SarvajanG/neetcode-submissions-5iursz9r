class Solution {
public:

    string encode(vector<string>& strs) {
        string result;
        for(const auto& s : strs) {
            result += s + 'Z';
        }
        cout << result;
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        string curWord;
        for (const auto& c : s) { 
            if (c == 'Z') {
                result.push_back(curWord);
                curWord = "";    
            } else {
                curWord += c;
            }
            
        }
        return result;
    }
};
