class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        combo_len = len(words)
        left = 0
        right = combo_len * word_len
        result = []
        while right <= len(s):
            substr = s[left:right]
            # print(substr)
            # creating dict
            dct = {}
            for word in words:
                if word in dct:
                    dct[word] += 1
                else:
                    dct[word] = 1
            flag = True
            for i in range(0, combo_len * word_len, word_len):
                cur_word = substr[i:i + word_len]
                # print(cur_word)
                if cur_word in dct:
                    dct[cur_word] -= 1
                    # print(dct)
                else:
                    flag = False
                    break

            for val in dct.values():
                if val != 0:
                    flag = False
                    break

            if flag:
                result.append(left)
            left += 1
            right += 1
        return result


