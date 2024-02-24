# Rotate 2D Matrix 
Rotating a 2D matrix refers to reorganizing its elements according to a specific pattern, typically by swapping adjacent elements along diagonals or performing cycles to achieve a 90-degree clockwise or counterclockwise transformation. 
> In Python, this can be accomplished via simple operations on lists representing each row of the matrix. For example, to rotate a 2D matrix 90 degrees clockwise, you can use the following concise one-line expression:
```python
def rotate_matrix(matrix):
    return list(zip(*matrix[::-1]))
```
> This code uses Python's zip() function to transpose the matrix and then reverses the resulting rows using slicing syntax [::-1]. Other methods exist, such as loop-based approaches, but the one-liner presented here offers simplicity and efficiency

## Credits
 * [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
 * [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
 * [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
 * [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
 * [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)
 * [Mock Technical Interview](https://www.youtube.com/watch?v=yM9Xbi-MigE)

## Contact
 * [Twitter](https://www.twitter.com/sakhilelindah) / [Github](https://github.com/sakhi-4096) / [Mail](mailto:sakhilelindah@protonmail.com)
