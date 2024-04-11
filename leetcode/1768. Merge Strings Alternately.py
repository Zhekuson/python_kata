class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))

        if len(word1) > len(word2):
            flag = "w1"
        else:
            flag = "w2"

        result = ""
        for i in range(0, min_len):
            result += word1[i] + word2[i]

        if flag == "w1":
            result += word1[min_len:]
        else:
            result += word2[min_len:]

        return result