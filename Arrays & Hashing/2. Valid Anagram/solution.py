from collections import Counter
class Solution:
    def isAnagram(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        count_a = Counter(a)
        count_b = Counter(b)
        for letter in count_a.keys():
            if not count_b.get(letter) or count_a[letter] != count_b[letter]:
                return False
        return True