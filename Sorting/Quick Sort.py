# # Time Complexity:
# O(nlogn) in average case
# O(n^2) in worst case
# # Space complexity is: O(1) in-place
## https://www.youtube.com/watch?v=0SkOjNaO1XY

# step1:pivot--->partition into left and right sublist
# step2: sort the left and right sublist of the list
# step3: divide and conquar stratagy
# pivot is at the correct postition in the final, sorted array, all the items at left are smaller, at right are larger

def partition(self, arr, l, r):
    pivot = arr[r]
    i = l - 1
    # i always points to the last element less than pivot
    # j is the current element we are examing
    for j in range(l, r):
        if arr[j] <= pivot:
            # first increase i, then swap
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # put pivot to the right postion
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    # return the index of pivot
    return i + 1


# the list between l and r will be sorted
def quick_sort(self, arr, l, r):
    # base case:
    if l >= r:
        return
    p = self.partition(arr, l, r)
    # the element at p is at the right order,
    # so we only need to sort its left and right part
    self.quick_sort(arr, l, p - 1)
    self.quick_sort(arr, p + 1, r)
