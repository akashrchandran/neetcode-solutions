from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            wordMap[''.join(sorted(word))].append(word)
        return wordMap.values()