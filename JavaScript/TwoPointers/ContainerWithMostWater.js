/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let res=0, lp=0, rp=height.length-1;
    while (lp < rp) {
        res = Math.max(res, Math.min(height[lp], height[rp]) * (rp-lp))
        height[lp] > height[rp] ? rp-- : lp++;
    }
    return res;
};
