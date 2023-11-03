# [1. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## Intuition
The problem asks us to determine whether a given string is a palindrome. A palindrome is a phrase that reads the same forward and backward when you remove non-alphanumeric characters and convert all uppercase letters to lowercase. To solve this problem, we need to compare the characters from the beginning and the end of the string while ignoring non-alphanumeric characters.

## Approach
1. Initialize two pointers, `l` and `r`, where `l` starts from the beginning of the string and `r` starts from the end of the string.
2. Use a while loop to iterate as long as `l` is less than `r`.
3. Inside the loop, use inner while loops to skip non-alphanumeric characters. Increment `l` while `s[l]` is not alphanumeric, and decrement `r` while `s[r]` is not alphanumeric.
4. After skipping non-alphanumeric characters, compare `s[l].lower()` with `s[r].lower()`. If they are not equal, return `False` because the string is not a palindrome.
5. If the characters are equal, increment `l` and decrement `r` to continue checking the next pair of characters.
6. If the while loop completes without returning `False`, it means the string is a palindrome, so return `True`.

## Complexity
- Time complexity: O(N), where N is the length of the input string `s`. We process the string once from both ends.
- Space complexity: O(1) as we use a constant amount of extra space for the pointers and variables.


## Runtime
![Solution](image.png)


## Leetcode Solution Post Link
> 