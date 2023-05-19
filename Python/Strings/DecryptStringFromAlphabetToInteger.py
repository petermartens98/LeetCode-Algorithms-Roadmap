class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Solution 1
        '''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        i = 0
        
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # Two-digit mapping
                digit = int(s[i:i + 2])
                i += 3
            else:
                # Single-digit mapping
                digit = int(s[i])
                i += 1
            
            result += alphabet[digit - 1]
        
        return result
        '''
        # Solution 2
        '''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        i = 0
        while i < len(s):
            digit = int(s[i:i+2]) if i+2 < len(s) and s[i+2] == '#' else int(s[i])
            result += alphabet[digit - 1]
            i += 3 if i+2 < len(s) and s[i+2] == '#' else 1
        return result
        '''
        # Solution 3
        '''
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        result = ''
        i = 0
        while i < len(s):
            digit = int(s[i:i+2]) if i+2 < len(s) and s[i+2] == '#' else int(s[i])
            result += alphabet[digit - 1]
            i += 3 if digit > 9 else 1
        return result
        '''
        # Solution 4
        '''
        alphabet, res, i = 'abcdefghijklmnopqrstuvwxyz', '', 0
        while i < len(s):
            digit = int(s[i:i+2]) if i+2 < len(s) and s[i+2] == '#' else int(s[i])
            res += alphabet[digit - 1]
            i += 3 if digit > 9 else 1
        return res
        '''
        # Solution 5
        '''
        alphabet, res, i = 'abcdefghijklmnopqrstuvwxyz', '', 0
        while i < len(s): digit = int(s[i:i+2]) if i+2 < len(s) and s[i+2] == '#' else int(s[i]); res += alphabet[digit - 1]; i += 3 if digit > 9 else 1
        return res
        '''
