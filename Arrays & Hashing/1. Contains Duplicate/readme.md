# [1. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Intuition
The intuition behind solving this problem is to check for the presence of duplicate elements in the given array.

## Approach
The approach involves converting the given array into a set, which automatically removes duplicate elements. By comparing the length of the original array with the length of the set, we can determine whether there are any duplicates. If the lengths are different, it implies the presence of duplicates.

## Complexity
- Time complexity: $$O(n)$$, where \(n\) is the number of elements in the input array. Constructing the set and comparing lengths both take linear time.
- Space complexity: $$O(n)$$, where \(n\) is the number of elements in the input array. The set used for duplicate detection can potentially have \(n\) elements.


## Code
```
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        
```
## Runtime

![Alt text](image.png)


## Leetcode Solution Post Link
> [Python](https://leetcode.com/problems/contains-duplicate/solutions/4096768/simplest-python-solution-using-hashset-beats-99-59/)