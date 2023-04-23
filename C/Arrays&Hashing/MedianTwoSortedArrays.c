#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int numsLen = nums1Size + nums2Size;
    int allNums[numsLen];
    int i = 0, j = 0, k = 0;
    while (i < nums1Size && j < nums2Size) {
        if (nums1[i] < nums2[j]) {
            allNums[k++] = nums1[i++];
        }
        else {
            allNums[k++] = nums2[j++];
        }
    }
    while (i < nums1Size) {
        allNums[k++] = nums1[i++];
    }
    while (j < nums2Size) {
        allNums[k++] = nums2[j++];
    }
    if (numsLen % 2 == 1) {
        return allNums[(int)floor(numsLen/2)];
    }
    return (allNums[numsLen/2] + allNums[(numsLen/2) - 1])/2.0;
}
