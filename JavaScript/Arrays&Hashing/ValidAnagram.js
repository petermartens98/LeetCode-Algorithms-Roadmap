/**
 * https://leetcode.com/problems/valid-anagram/
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

// Solution 1
/**
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(N))
 * Time O(N * logN) | Space O(N)

var isAnagram = function(s, t) {
    const isEqual = s.length === t.length;
    if (!isEqual) return false;
    return reorder(s) === reorder(t);
};

const reorder = (str) => str
    .split('')
    .sort((a, b) => a.localeCompare(b))
    .join(''); 
*/

// Solution 2
/**
 * Hash Map - Frequency Counter
 * Time O(N) | Space O(N)
 */

 var isAnagram = (s, t, map = new Map()) => {
    const isEqual = s.length === t.length;
    if (!isEqual) return false;
    addFrequency(s, map);
    subtractFrequency(t, map);
    return checkFrequency(map);
};

const addFrequency = (str, map) => {
    for (const char of str) {
        const count = (map.get(char) || 0) + 1;
        map.set(char, count);  
    }
}

const subtractFrequency = (str, map) => {
    for (const char of str) {
        if (!map.has(char)) continue;
        const count = map.get(char) - 1;
        map.set(char, count);
    }
};

const checkFrequency = (map) => {
    for (const [ char, count ] of map) {
        const isEmpty = count === 0;
        if (!isEmpty) return false;
    }
    return true;
}
