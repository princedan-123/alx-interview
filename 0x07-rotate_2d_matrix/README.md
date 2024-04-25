<h3>0x07. Rotate 2D Matrix
Algorithm
Python </h3>
<p>Alx Backend short specialisation tutorial project on transponsing and rotation a two dimensional matrix.</p>
<p> Project will start Apr 22, 2024 6:00 AM, should end by Apr 26, 2024 6:00 AM
 Checker was released at Apr 23, 2024 6:00 AM
 An auto review will be launched at the deadline
 </p>
 <p>For the “0. Rotate 2D Matrix” project, you are tasked with implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python. Below are the key concepts and resources that you need to grasp in order to successfully complete this project.</p>

 <p>Concepts Needed:</p>
 <ul>
 <li>Matrix Representation in Python:

Understanding how 2D matrices are represented using lists of lists in Python.
Accessing and modifying elements in a 2D matrix.</li>
 <li>In-place Operations:

Performing operations on data without creating a copy of the data structure.
The importance of minimizing space complexity by modifying the matrix in place.</li>
 <li>Matrix Transposition:

Understanding the concept of transposing a matrix (swapping rows and columns).
Implementing matrix transposition as a step in the rotation process.</li>
 <li>Reversing Rows in a Matrix:

Manipulating rows of a matrix by reversing their order as part of the rotation process.</li>
 <li>Nested Loops:

Using nested loops to iterate through 2D data structures like matrices.
Modifying elements within nested loops to achieve the desired rotation.</li>
 </ul>
 <h3>Resources:</h3>
 <ul>
 <h5>Python Official Documentation:</h5>
 <li><a href='https://docs.python.org/3/tutorial/datastructures.html'>Data Structures (list comprehensions, nested list comprehension)</a></li>
 <li><a href='https://docs.python.org/3/tutorial/datastructures.html#more-on-lists'>More on Lists</a></li>
 <li><a href='https://docs.python.org/3/tutorial/datastructures.html#more-on-lists'>More on Lists</a></li>
 <h5>GeeksforGeeks Articles:</h5>
 <li><a href='https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/'>Inplace rotate square matrix by 90 degrees</a></li>
  <li><a href='https://www.geeksforgeeks.org/transpose-matrix-single-line-python/'>Transpose a matrix in Single line in Python</a></li>
  <h5>TutorialsPoint:</h5>
  <li><a href='https://www.tutorialspoint.com/python/python_lists.htm'>Python Lists for basics of list manipulation in Python</a></li>
 </ul>
 <p>By understanding these concepts and utilizing the provided resources, you will be able to approach the problem methodically, first transposing the matrix and then reversing each row to achieve a 90-degree clockwise rotation. This project not only tests your ability to manipulate 2D matrices but also challenges you to think about optimizing your solution to operate in-place, thus improving their problem-solving and algorithmic thinking skills in Python.</p>
 <h5>Requirements</h5>
 <ul>
 <li>Allowed editors: vi, vim, emacs</li>
 <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)</li>
 <li>All your files should end with a new line</li>
 <li>The first line of all your files should be exactly #!/usr/bin/python3</li>
 <li>A README.md file, at the root of the folder of the project, is mandatory</li>
 <li>Your code should use the pycodestyle style (version 2.8.0)</li>
 <li>You are not allowed to import any module</li>
 <li>All modules and functions must be documented</li>
 <li>All your files must be executable</li>
 </ul>
 <h5>Tasks</h5>
 <ul>
 <li>Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.</li>
"""
    jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
"""
 </ul>