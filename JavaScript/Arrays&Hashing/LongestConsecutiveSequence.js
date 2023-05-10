/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numSet = new Set(nums.sort((a, b) => a - b));
    let longestSeq = 0;
    for (let num of numSet) {
        if (!numSet.has(num - 1)) {
            let currentSeq = 1;
            while (numSet.has(num + currentSeq)) currentSeq++;
            longestSeq = Math.max(longestSeq, currentSeq);
        }
    }
    return longestSeq;
};
