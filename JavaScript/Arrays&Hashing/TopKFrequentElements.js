/** Solution 1
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}

var topKFrequent = function(nums, k) {
    const numCounts = {};
    for (const num of nums) {
        numCounts[num] = numCounts[num] + 1 || 1;
    }
    const sortedCounts = Object.entries(numCounts).sort((a, b) => b[1] - a[1]);
    const topK = sortedCounts.slice(0, k);
    return topK.map(([num]) => parseInt(num));
};
*/
// Solution 2 - Solution 1 condendsed
var topKFrequent = function(nums, k) {
    const numCounts = {};
    for (const num of nums) numCounts[num] = numCounts[num] + 1 || 1;
    return Object.entries(numCounts).sort((a, b) => b[1] - a[1]).slice(0, k).map(([num]) => parseInt(num));
};
