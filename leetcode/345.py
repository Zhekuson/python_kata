class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {
            "a", "e", "i", "o", "u",
            "A", "E", "I", "O", "U"
        }
        v_list = []
        p_list = []
        s_len = len(s)
        for i in range(s_len):
            if s[i] in vowels:
                v_list.append(s[i])
                p_list.append(i)

        result = list(s)
        for i in range(len(v_list)):
            result[p_list[i]] = v_list[len(v_list) - i - 1]
        return ''.join(result)

