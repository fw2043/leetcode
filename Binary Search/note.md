# some questions you might want to confirm:
## 0. the pivot is mid which is used to travel the items
## 1. is the list sorted or not(ascending or descending? like trictly increasing order
## 2. if the nums are unique or have duplicates
## 3. if it does not exist, what result do you want----return -1
## 4. running time of sorting a list:
list = [30, -10, 5, 10, 7] <br/>
list.sort()---> inplace sort <br/>
runtime complexity is O(N * logN) </br>
**O(1) < O(logn) < O(n) < O(nlogn)**</br>
**based on the runtime requirement, you caan choose which algorithm you can use: 
brute force/ binary search**
## 5.how long of this list, if it is not too long, you might be able to use O(N)-- BRUTE FORCE, like leetcode 1539
## 6. confirm the length of the list for mid = (left + right) // 2 ---> not overflow, to avoid overflow you can use: 
mid = l + (r - l) // 2
## 6. how to control just search left/right part---> adding one viable e.g leftBias-----> leetcode 34

## 7. Find the unique data structues you can use> like 362: Design Hit Counter,---queue(FIFO)



