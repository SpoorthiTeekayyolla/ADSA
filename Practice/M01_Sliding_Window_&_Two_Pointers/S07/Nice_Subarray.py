'''
1763
1652

'''
def longestNiceSubstring(self, s: str) -> str:
        if len(s)< 2:
            return ""
        uniq = set(s)
        for i,ch in enumerate(s):
            if ch.lower() in uniq and ch.upper() in uniq:
                continue 
            left_str = self.longestNiceSubstring(s[:i])
            right_str = self.longestNiceSubstring(s[i+1:])

            return left_str if len(left_str) >= len(right_str) else right_str 
        return s
    
    