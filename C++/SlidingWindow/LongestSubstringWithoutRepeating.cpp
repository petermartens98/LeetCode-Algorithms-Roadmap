// Solution 1 - Brute Force
/*
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() < 2) {
            return s.length();
        }
        int output = 1;
        for (int i = 0; i < s.length(); i++) {
            unordered_set<char> chars;
            chars.insert(s[i]);
            for (int j = i + 1; j < s.length(); j++) {
                if (chars.count(s[j])) {
                    break;
                } else { 
                    chars.insert(s[j]);
                }
                output = max(output, (int)chars.size());
            }
        }
        return output;
    }
};
*/
// Solution 2 - Sliding Window
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        if (n < 2) { return n; }
        int i = 0, j = 0, output = 0;
        int count[256] = {0}; // ASCII character set
        while (j < n) {
            count[s[j]]++;
            while (count[s[j]] > 1) { // Repeating character found
                count[s[i]]--;
                i++;
            }
            output = max(output, j - i + 1);
            j++;
        }
        return output;
    }
};
