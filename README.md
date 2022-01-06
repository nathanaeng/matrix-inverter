# matrix-inverter
Implementation of a matrix object in Python.

Given a matrix A, possible matrix operations include transpose(A) and inverse(A).

----

Methods of the matrix object:
--

clean_str(): prints a visual representation of the matrix with better spacing

get_det(): returns the determinant of the matrix

has_inverse(): returns True if the matrix is invertible and False otherwise

transpose(): returns the transposed matrix

get_inverse(): returns the inverse of the matrix

----

By default, matrix_inverter.py will ask for the user to input a matrix, and it will print the inverse of that matrix, if it is invertible.

test_matrix_inverter.py contains a small test suite - this will be updated to be more extensive in the future.
