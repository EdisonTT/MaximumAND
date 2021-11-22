# MaximumAND
Programming Question.

## The Question
Given an array **`A[]`** of **`N`** elements, you can pick at most one element of the array and increment or decrement it by any value. The task is to maximize the **`AND`** of the resulting array.

Note: **`AND`** of the array is defined as the bitwise **`AND(&)`** of all array elements.

## Sample Input and Output Explained

- Consider the input array: **`A = [1,2,3]`**. Taking **`AND`** between the elements will give: **`1&2&3=0`**. Replace the first element, that is **`1`** with **`2`** will result in **`2&2&3=2`**. Thus according to the given instruction in the question, the maximum value is **`2`**. Those who are not familiar with bitwise **`AND(&)`**, take a look at [here](https://www.geeksforgeeks.org/python-bitwise-operators/).
- The input array **`A = [10,10]`**. The Maximum of the **`AND`** is **`10`**. No change is required.

## The Strategy

This section intends to explain the strategy followed in the code `solution.py`. The first move is to create a matrix. The number of rows in the matrix is the same as the number of elements in the array. The number of columns is the number of bits required by the largest number in the array. Let's do a deep dive into the construction of the matrix.

- Find the largest number in the given array. In **python**, the inbuild method `max()` can be used.<br>
  For example, `max([4,8,11,27,29])` will give `29` as output.
- Convert that number into binary. In python, the inbuild method  `bin()` can be used.<br>
  For example, `bin(29)` will give `0b11101` as output. Note that the output is a binary string.
- The number of bits required for the largest number can be found as `len(bin(max_num))-2`. The `len()` method returns the number of items in an object. When the object is a string, the `len()` method returns the number of characters in the string.
For example, `len(bin(29))` will give `7` as output. Subtract `2` to get the number of bits required. `2` is subtracted to eliminate the count of `0b`.
- Now the dimention of the matrix is obtained. For the example followed so far, the dimention is `5X5`.
    | Number | Binary |
    | :------: | :-------: |
    |4 | 00100 |
    |8 | 01000 |
    |11| 01011 | 
    |27| 11011 |
    |29| 11101 |
- The matrix is given by:<br>
  
