#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> allNums(nums1);
        allNums.insert(allNums.end(), nums2.begin(), nums2.end());
        sort(allNums.begin(), allNums.end());
        int numsLen = allNums.size();
        if (numsLen % 2 == 1) {
            return allNums[static_cast<int>(floor(numsLen/2))];
        }
        return (allNums[numsLen/2] + allNums[(numsLen/2) - 1])/2.0;
    }
};
