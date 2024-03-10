<p> This is a tutorial project with the aim of creating a list of lists that represents rows in Pascal's Triangle</p>
<h3>Resources</h3>
<ul>
<li><a href="https://www.cuemath.com/algebra/pascals-triangle/">What is Pascal’s triangle</a></li>
<li><a href="https://www.youtube.com/watch?v=0iMtlus-afo">Pascal’s Triangle - Numberphile</a></li>
<li><a href="https://builtin.com/data-science/python-algorithms">What are Python Algorithms</a></li>
</ul>

<h3>MUST KNOW </h3>
<p>To successfully complete this project, you should revise the following Python concepts:</p>
<ul>
<li>Lists and List Comprehensions:

Understand how to create, access, modify, and iterate over lists.
Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal’s Triangle.
</li>
<li>Functions:

Know how to define and call functions.
Pass parameters and return values, particularly how to return a list of lists representing Pascal’s Triangle.</li>
<li>Conditional Statements:

Apply if, elif, and else conditions to implement logic based on the position within Pascal’s Triangle (e.g., the edges of the triangle always being 1).</li>
<li>Recursion (Optional):

While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal’s Triangle.
Recognize base cases and recursive cases for a function that generates the triangle’s rows.</li>
<li>Arithmetic Operations:

Perform addition, a fundamental operation for calculating each element of Pascal’s Triangle as the sum of the two elements directly above it.</li>
<li>Indexing and Slicing:

Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.</li>
<li>Memory Management:

Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.</li>
<li></li>Error and Exception Handling (Optional):

Use try-except blocks as needed to handle potential errors, such as invalid input types or values.
<li>Efficiency and Optimization:

Consider the time and space complexity of different approaches to generating Pascal’s Triangle.
Evaluate and apply optimizations to improve the performance of the solution.</li>
</ul>
<em>By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal’s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.</em>
<p>TASK</p>
<ul>
<li>Pascal's Triangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer</li>
</ul>
<h3> Implementation (pascal_triangle)</h3>
<p>
In my implementation a global reference called triangle to a list was created to hold the rows of the triangle.
A function called baseline was defined to create the first two rows of the triangle.
Another function create_row was defined to generate a new row from adding elements in the previous row.
The Implementation returns a list of lists.
The 0-main.py script prints the rows(list) in the triangle
</p>
