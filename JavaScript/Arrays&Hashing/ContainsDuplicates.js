/**
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */
 // Solution 1
 /*
var containsDuplicate = function(nums) {
    var uniques = [];
    for (var i = 0; i < nums.length; i++) {
        if (uniques.indexOf(nums[i]) !== -1) {
            return true;
        }         
        uniques.push(nums[i]);
    }
    return false;
};
*/

// Solution 2
/**
 * Brute Force - Linear Search
 * Time O(N^2) | Space O(1)
 */
 /*
var containsDuplicate = function(nums) {
    for (let r = 0; r < nums.length; r++) {
        for (let l = 0; l < r; l++) { 
            const isDuplicate = nums[l] === nums[r];
            if (isDuplicate) return true;
        }
    }
    return false;
};
*/

// Solutiion 3
/**
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(N))
 * Time O(N * log(N)) | Space O(1)

var containsDuplicate = (nums) => {
    nums.sort((a, b) => a - b); // sorts the elements of an array nums in ascending order
    return hasDuplicate(nums);
}

const hasDuplicate = (nums) => {
    for (let curr = 0; curr < (nums.length - 1); curr++) {
        const next = (curr + 1);

        const isNextDuplicate = nums[curr] === nums[next];
        if (isNextDuplicate) return true;
    }
    return false;
}
*/

// Solution 4
/**
 * Hash Set
 * Time O(N) | Space O(N)

var containsDuplicate = (nums) => {
    const numsSet = new Set(nums);
    const isEqual = numsSet.size === nums.length;
    return !isEqual;
};
*/

// Solution 4 - Condensed
/*
var containsDuplicate = (nums) => { return !((new Set(nums)).size === nums.length); };
*/

// Solution 5
/**
 * Hash Set - Early Exit
 * Time O(N) | Space O(N)
 */
var containsDuplicate = (nums, numsSet = new Set()) => {
    for (const num of nums) {
        if (numsSet.has(num)) return true;
        numsSet.add(num);
    }
    return false;
};

