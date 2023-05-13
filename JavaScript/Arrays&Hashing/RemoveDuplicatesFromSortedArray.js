/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let res = [];
    for (let i = 0; i < nums.length; i++){
        if (!res.includes(nums[i])) {
            res.push(nums[i]);
        }
    }
    nums.splice(0, nums.length, ...res);
    return res.length;
};
