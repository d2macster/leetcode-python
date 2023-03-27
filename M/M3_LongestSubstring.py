class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        SL = 0
        CharHash = {}
        prev_id = -1
        for cid, c in enumerate(s):
            if c in CharHash:
                prev_id = max(prev_id, CharHash[c])
            SL = max(SL, cid - prev_id)
            CharHash[c] = cid

        return SL