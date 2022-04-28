class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def get_dct(s: str):
            available = {}
            for char in s:
                if char in available.keys():
                    available[char] += 1
                else:
                    available[char] = 0
            return available

        common = get_dct(chars)
        summ = 0
        for item in words:
            word_dct = get_dct(item)
            flag = True
            for key in word_dct.keys():
                if (key not in common) or (common[key] < word_dct[key]):
                    flag = False
                    break
            if flag:
                summ += len(item)
        return summ

