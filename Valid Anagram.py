class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Solved using a hash table"""
        letters = {}

        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        for letter in t:
            if letter not in letters:
                return False
            else:
                letters[letter] -= 1

        for counts in letters.values():
            if counts != 0:
                return False

        return True
