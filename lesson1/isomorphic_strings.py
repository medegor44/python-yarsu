class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charsMapping = dict[str, str]()
        reverseMapping = dict[str, str]()

        for i in range(len(s)):
            if s[i] not in charsMapping and t[i] not in reverseMapping: 
                charsMapping[s[i]] = t[i]
                reverseMapping[t[i]] = s[i]
                continue

            if (
                (s[i] in charsMapping and charsMapping[s[i]] != t[i]) or 
                (t[i] in reverseMapping and reverseMapping[t[i]] != s[i])
            ):
                return False
        
        return True

print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
