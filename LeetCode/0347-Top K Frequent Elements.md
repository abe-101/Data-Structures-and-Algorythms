---
title: 0347-Top K Frequent Elements
updated: 2022-07-10 15:55:55Z
created: 2022-07-10 15:54:32Z
source: https://leetcode.com/problems/top-k-frequent-elements/
tags:
  - arrays and hashing
  - blind 75
  - medium
  - python
---

347\. Top K Frequent Elements

Medium

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]

```

**Constraints:**

- `1 <= nums.length <= 10<sup>5</sup>`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

**Solution:**

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
```
Time Complexity: O(n)
Space Complexity: O(n)