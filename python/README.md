# LeetCode Python Solutions

This repository contains solutions to various LeetCode problems, organized by topic and implemented in Python. Each solution is provided with a brief description of the problem and a sample usage example.

## Table of Contents

- [Overview](#overview)
- [Arrays & Hashing](#arrays--hashing)
- [Two Pointers](#two-pointers)
- [Stack](#stack)
- [usage] (#usage)

## Overview

This repository aims to provide clear and efficient solutions to common LeetCode problems, grouped by topic for easier navigation and understanding. Each solution is accompanied by a problem description and a sample usage example to help users understand the implementation.

## Arrays & Hashing

1. **217) Contains Duplicate**
   - **Problem:** Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.
   - **Example:**
     ```python
     print(containsDuplicate([1,2,3,2]))  # Output: True
     ```

2. **242) Valid Anagram**
   - **Problem:** Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
   - **Example:**
     ```python
     print(isAnagram("anagram", "nagaram"))  # Output: True
     ```

3. **1) Two Sum**
   - **Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
   - **Example:**
     ```python
     print(twoSum([2,7,11,15], 9))  # Output: [0, 1]
     ```

4. **49) Group Anagrams**
   - **Problem:** Given an array of strings `strs`, group the anagrams together.
   - **Example:**
     ```python
     print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
     # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
     ```

5. **347) Top K Frequent Elements**
   - **Problem:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
   - **Example:**
     ```python
     print(topKFrequent([1,2], 2))  # Output: [1, 2]
     ```

6. **238) Product of Array Except Self**
   - **Problem:** Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
   - **Example:**
     ```python
     print(productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
     ```

7. **36) Valid Sudoku**
   - **Problem:** Determine if a 9x9 Sudoku board is valid according to specific rules.
   - **Example:**
     ```python
     print(isValidSudoku([
         ["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]
     ]))  # Output: True
     ```

8. **128) Longest Consecutive Sequence**
   - **Problem:** Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
   - **Example:**
     ```python
     print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
     ```

## Two Pointers

1. **125) Valid Palindrome**
   - **Problem:** Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.
   - **Example:**
     ```python
     print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
     ```

2. **167) Two Sum 2 - Input Array Is Sorted**
   - **Problem:** Given a 1-indexed array of integers `numbers` that is already sorted, find two numbers that add up to a specific target number.
   - **Example:**
     ```python
     print(twoSum([2,3,4], 6))  # Output: [1, 3]
     ```

3. **15) 3Sum**
   - **Problem:** Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that they add up to `0`.
   - **Example:**
     ```python
     print(threeSum([-1,0,1,2,-1,-4]))
     # Output: [[-1, -1, 2], [-1, 0, 1]]
     ```

4. **11) Container With Most Water**
   - **Problem:** Given an integer array `height`, find two lines that together with the x-axis form a container that can store the most water.
   - **Example:**
     ```python
     print(maxArea([1,8,100,2,100,4,8,3,7]))  # Output: 200
     ```

5. **42) Trapping Rain Water**
   - **Problem:** Given `n` non-negative integers representing an elevation map, compute how much water it can trap after raining.
   - **Example:**
     ```python
     print(trap([4,2,0,3,2,5]))  # Output: 9
     ```

## Stack

1. **20) Valid Parentheses**
   - **Problem:** Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
   - **Example:**
     ```python
     print(isValid("()(){}[]"))  # Output: True
     ```
## usage
- clone the repo
- open leetcodeWithPython.py
- and call the function that you want