/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;
    for (let i = 0; i < prices.length; i++) {
        let price = prices[i];
        if (price < minPrice) minPrice = price; 
        else maxProfit = Math.max(maxProfit, price - minPrice);
    }
    return maxProfit;
};
