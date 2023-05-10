/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let n = nums.length;
    let leftProds = new Array(n).fill(1); // array to store products of all elements to the left of each element
    let rightProds = new Array(n).fill(1); // array to store products of all elements to the right of each element
    let res = new Array(n).fill(1); // array to store the final results
    for (let i = 1; i < n; i++) {
        leftProds[i] = leftProds[i-1] * nums[i-1]; // compute the product of all elements to the left of each element
    }
    for (let i = n-2; i >= 0; i--) {
        rightProds[i] = rightProds[i+1] * nums[i+1]; // compute the product of all elements to the right of each element
    }
    for (let i = 0; i < n; i++) {
        res[i] = leftProds[i] * rightProds[i]; // combine the left and right products to get the final result
    }
    return res;
};
