class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def check_prefix(s, prefix):
            i = len(s)
            p_len = len(prefix)
            while i > 0:
                if s[:p_len] == prefix:
                    i -= p_len
                    s = s[p_len:]
                else:
                    return False
            return True

        L1 = len(str1)
        L2 = len(str2)
        min_len = min(L1, L2)
        i = 0
        max_prefix = ""
        while i < min_len and str1[:i + 1] == str2[:i + 1]:
            cur_prefix = str1[:i + 1]
            if check_prefix(str1, cur_prefix) and check_prefix(str2,
                                                               cur_prefix):
                max_prefix = cur_prefix
            i += 1

        return max_prefix





