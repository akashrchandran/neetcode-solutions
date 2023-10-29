from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = max(arr)
        for i in range(len(arr)-1):
            if arr[i] == cur_max:
                cur_max = max(arr[i+1:])
            arr[i] = cur_max
        arr[-1] = -1
        return arr