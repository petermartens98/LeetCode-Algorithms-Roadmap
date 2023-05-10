/**
 * Brute Force - Linear Search
 * Time O(N^2) | Space O(1)
 * https://leetcode.com/problems/two-sum/
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}

var twoSum = (nums, target) => {
    for (let curr = 0; curr < nums.length; curr++) { 
        const complement = target - nums[curr];

        for (let next = (curr + 1); next < nums.length; next++) { 
            const num = nums[next];

            const isTarget = num === complement
            if (isTarget) return [ curr, next ];
        }
    }

    return [ -1, -1 ];
}
*/

/** Hash Map Solution
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
function twoSum(nums, target) {
    const prevMap = {};
    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        const diff = target - n;
        if (diff in prevMap) {
            return [prevMap[diff], i];
        }
        prevMap[n] = i;
    }
    return [];
}
*/
