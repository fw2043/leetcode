"""
RAM
Before diving into what an array is, it is important to understand what a data structure is to begin with.

Simply put, data structures are a way to store data in an efficient manner inside the Random Access Memory, hereafter called "RAM".
An array is a collection of ordered, contiguous group of elements. If we wanted to store three integers - 1, 3, 5 in our RAM,
an array can be used. The question here is how does the computer store these numbers in the RAM if it only understands data in terms of bits - 0s and 1s.
This requires understanding of the RAM. Computers these days have RAM in terms of gigabytes.
In fact, the computer you are using to view this course might have 8 GB (109 bytes) of RAM. 1 byte = 8 bits. A bit is a 0 OR a 1.

Integers commonly occupy 4 bytes (32 bits) in memory. An address and a value gets associated with an integer upon storing it in RAM.
An address is just a distinct location that each one of the values is stored at. Each value is stored contiguously in the RAM, just like an array.
Each character takes 8 bits of space, 1 byte, hence the addresses are 1 byte apart.
"""
########################################## Static Array ################################################################
##########################################################################################################################
# initialize myArray
myArray = [1,3,5]

# access an arbitrary element, where i is the index of the desired value
myArray[i]

# As long as the index of an element is known, the access is instant: O(1)

# Traversing through an array: O(n)
for i in range(len(myArray)):
    print(myArray[i])

# OR
i = 0
while i < len(myArray):
    print(myArray)
    i += 1

# Static array: rrays have an allocated size when initialized. This means that the size of the array cannot change after its initialization.

# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    # Overwrite last element with some default value.
    # We would also consider the length to be decreased by 1.
    if length > 0:
        arr[length - 1] = 0


# Deleting at an ith index
# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted


# Inserting at the end of the array
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# Inserting at the ith index
# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    # Insert at i
    arr[i] = n



########################################## Dynamic Array ################################################################
##########################################################################################################################
# understand why we need to double size when we create an array
#Mechanics of dynamic arrays
"""When inserting into a dynamic array, the operating system finds the next empty space and pushes the element into it. 
For the sake of an example, let’s take an array of size 
3 and push elements into it until we run out of space

Since the array is dynamic, adding another element when we run out of capacity is achieved by copying over the values to a new array that is double the original size
- this means that the resulting array will be of size 6 and will have new space allocated for it in memory.
When all the elements from the first array have been copied over, it does not make sense to keep it in memory - this space will be deallocated.
"""
## Why double the capacity?
"""
https://neetcode.io/courses/dsa-for-beginners/3
"""












