/** Solution 1
 * @param {string} s
 * @return {boolean}
 
const isValid = function(s) {
  const stack = [];
  const closeToOpen = {
    ")": "(",
    "]": "[",
    "}": "{"
  };

  for (let i = 0; i < s.length; i++) {
    const c = s.charAt(i);
    if (closeToOpen.hasOwnProperty(c)) {
      if (stack.pop() !== closeToOpen[c]) {
        return false;
      }
    } else {
      stack.push(c);
    }
  }

  return stack.length === 0;
};
*/

// Solution 2

const isValid = (s) => {
  const stack = [];
  const closeToOpen = { ")": "(", "]": "[", "}": "{" };
  for (let i = 0; i < s.length; i++) {
    if (closeToOpen[s[i]]) {
      if (stack.pop() !== closeToOpen[s[i]]) return false;
    } else stack.push(s[i]);
  }
  return stack.length === 0;
};

