class Solution:
    def reverseVowels(self, s: str) -> str:
        # Solution 1
        '''
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s_vowels = []
        for char in s:
            if char in vowels: s_vowels.insert(0, char)
        vc = 0
        res = ""
        for i, char in enumerate(s):
            if char in vowels:
                res += s_vowels[vc]
                vc+=1
            else:
                res += char
        return res
        '''
        # Solution 2: Two Pointers
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s_list = list(s)
        l, r = 0, len(s_list) - 1 
        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] in vowels: r -= 1
            elif s_list[r] in vowels: l += 1
            else:
                l += 1
                r -= 1
        return "".join(s_list)
