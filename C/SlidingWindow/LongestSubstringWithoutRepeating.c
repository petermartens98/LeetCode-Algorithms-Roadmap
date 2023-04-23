// Solution 1 - Brute Force
/*
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    if (strlen(s) < 2) {
        return strlen(s);
    }
    int output = 1;
    for (int i = 0; i < strlen(s); i++) {
        char chars[256] = {0};
        chars[s[i]] = 1;
        for (int j = i + 1; j < strlen(s); j++) {
            if (chars[s[j]]) {
                break;
            } else {
                chars[s[j]] = 1;
            }
            output = (output > (j - i + 1)) ? output : (j - i + 1);
        }
    }
    return output;
}
*/
// Solution 2 - Sliding Window
#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    if (n < 2) { return n; }
    int i = 0, j = 0, output = 0;
    int count[256] = {0}; // ASCII character set
    while (j < n) {
        count[s[j]]++;
        while (count[s[j]] > 1) { // Repeating character found
            count[s[i]]--;
            i++;
        }
        output = (output > (j - i + 1)) ? output : (j - i + 1);
        j++;
    }
    return output;
}
