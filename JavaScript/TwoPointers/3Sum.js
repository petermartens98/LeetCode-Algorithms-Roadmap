/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 // Solution 1
 /*
var threeSum = function(nums) {
    const res = [];
    if (nums.length < 3) return res;
    nums.sort((a,b)=>a-b);
    for(let i=0; i<nums.length; i++) {
        if (nums[i]>0) break;
        if (i>0 && nums[i]===nums[i-1]) continue;
        let start=i+1, end=nums.length-1;
        while(start<end){
            const sum = nums[i]+nums[start]+nums[end];
            if (sum === 0) {
                res.push([nums[i], nums[start], nums[end]])
                start += 1;
                end -= 1;
                while(start<end && nums[start]===nums[start-1]) start+=1;
                while(start<end && nums[end]===nums[end+1]) end-=1;
            } 
            else if (sum<0) start+=1;
            else if (sum>0) end-=1;
        }
    }
    return res;
}
*/
// Solution 2 - Solution 1 Optimized and condensed
function threeSum(nums) {
    if (nums.length < 3) return [];
    nums.sort((a, b) => a - b);
    if (nums[0] > 0 || nums[nums.length - 1] < 0) return [];
    const res = [];
    for (let i = 0; i < nums.length - 2; i++) {
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        let start = i + 1, end = nums.length - 1;
        while (start < end) {
            const sum = nums[i] + nums[start] + nums[end];
            if (sum === 0) {
                res.push([nums[i], nums[start], nums[end]]);
                start++; end--;
                while (start < end && nums[start] === nums[start - 1]) start++;
                while (start < end && nums[end] === nums[end + 1]) end--; 
            } 
            else if (sum < 0) start++;
            else end--;
        }
    }
    return res;
}
