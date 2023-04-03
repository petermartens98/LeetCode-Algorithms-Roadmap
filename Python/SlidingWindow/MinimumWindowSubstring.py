class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Solution 1
        '''
        res, resLen = [-1, -1], float("infinity")
        if t == "": return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        '''
        # Solution 2 ~ Solution 1 Condensed
        res, resLen = [-1, -1], float("infinity")
        if t == "": return ""
        countT, window, have, need = {}, {}, 0, len(set(t))
        for c in t: countT[c] = countT.get(c, 0) + 1
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in countT and window[s[r]] == countT[s[r]]: have += 1
            while have == need:
                if r - l + 1 < resLen: res, resLen = [l,r], r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
