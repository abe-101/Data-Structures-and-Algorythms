## Sorted Squares 

**Level**: Easy 

Given a sorted array in non-decreasing order, return an array of squares of each number, also
in non-decreasing order. For example:  

[-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]  

How can you do it in O(n) time?  


Questions to Clarify:
Q. Can there be both negative and positive numbers?  
A. Yes.  

Q. Should the output  be a new array or the exiting array modified?  
A. Both are fine.  


## Solution
Sorting approach: We can calculate the square and then sort it. That would take O(nlogn(n)). the interviewer is looking for a solution with O(n) time.

There is a patern in the array. The largest squares will be at either end. so we can look at either end grad the larger in move inward.

**Pseudocode**:
```
int start = 0, end = n.length-1;

int[] result = size of a

while start <= end
    if abs(a[start]) > abs(a[end])
        add square(a[start]) to the end of result
        increase start by 1
    else
        add square(a[end]) to the end of result
        decrease end by 1
return result
```
**Test Cases**:
Edge Cases: Empty array, null array  
Base Cases: single element (+ve/-ve)  
Regular Case: only +ve elements, only -ve elements, both +ve/-ve  

Time Complexity: O(n)  
Space Complexity: O(n)  
