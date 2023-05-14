/** Solution 1
 * @param {string} s
 * @param {number} k
 * @return {number}
var characterReplacement = function(s, k) {
    let count = {};
    let res = 0, l = 0;
    for (let r = 0; r < s.length; r++) {
        count[s[r]] = 1 + (count[s[r]] || 0);
        while ((r - l + 1) - Math.max(...Object.values(count)) > k) {
            count[s[l]]--;
            l++;
        }
        res = Math.max(res, r - l + 1);
    }
    return res;
};

*/

// Solution 2
/*
var characterReplacement = function(s, k) {
    let count = Array(26).fill(0);
    let res = 0, l = 0, maxCount = 0;
    for (let r = 0; r < s.length; r++) {
        const idx = s.charCodeAt(r) - 65;
        count[idx]++;
        maxCount = Math.max(maxCount, count[idx]);
        while ((r - l + 1) - maxCount > k) {
            count[s.charCodeAt(l) - 65]--;
            l++;
        }
        res = Math.max(res, r - l + 1);
    }
    return res;
};
*/
// Solution 3
function characterReplacement(s, k) {
    const count = {};
    let res = 0, l = 0, maxCount = 0;
    for (let r = 0; r < s.length; r++) {
        const c = s[r];
        count[s[r]] = (count[c] || 0) + 1;
        maxCount = Math.max(maxCount, count[c]);
        if (r - l + 1 - maxCount > k) {
            count[s[l]]--;
            l++;
        }
        res = Math.max(res, r - l + 1);
    }
    return res;
};
