class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for letter in magazine:
            if letter in magazine_dict:
                magazine_dict[letter] += 1
            else:
                magazine_dict[letter] = 1

        for letter in ransomNote:
            if not (letter in magazine_dict):
                return False
            else:
                magazine_dict[letter] -= 1
        for value in magazine_dict.values():
            if value < 0:
                return False
        return True