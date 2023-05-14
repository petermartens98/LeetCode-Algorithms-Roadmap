/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let tempChars = [];
    let tempCount = 0; 
    let res = 0;
    for (let char of s) {
        let index = tempChars.indexOf(char);
        if (index !== -1) {
            tempChars.splice(0, index + 1);
            tempCount = tempChars.length;
        }
        tempChars.push(char);
        tempCount++;
        res = Math.max(res, tempCount);
    }
    return res;
};
