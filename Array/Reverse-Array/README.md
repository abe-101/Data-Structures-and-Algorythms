## Reverse an Array

**Level**: easy

Questions to Clarify:
Q. Can we allocate a new array?
A. No

## Solution
Swap both end

**Pseudocode**:
```
int start = 0, end = a.length-1
while start < end
    swap a[start] and [end]
    increase start, decrease end

```
**Test Cases**:
Edge Cases: empty array, null array  
Base Cases: single element  
Regular Case: 2 elements, 3 elements, odd elements, even elements  

Time Complexity: O(n) aka linear time  

Space Complexity: O(1) aka constant space

