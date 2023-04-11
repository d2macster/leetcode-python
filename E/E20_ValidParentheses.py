class Solution:
    def isValid(self, s: str) -> bool:
        L = len(s)
        if L <= 1:
            return False
        if L % 2 == 1:
            return False
        q = []
        openSet = {'(', '[', '{'}
        for ch in s:
            if ch in openSet:
                q.append(ch)
                continue
            if not q:
                return False
            if ch == ')' and q[-1] != '(':
                return False
            if ch == ']' and q[-1] != '[':
                return False
            if ch == '}' and q[-1] != '{':
                return False
            q.pop()
        return len(q) == 0
