# matrix-inverter
Implementation of a matrix object in Python.

Given a matrix A, possible matrix operations include transpose(A) and inverse(A).

----

Methods of the matrix object:
--

formatted(): returns a string containing a visual representation of the matrix with better spacing

get_det(): returns the determinant of the matrix

has_inverse(): returns True if the matrix is invertible and False otherwise

transpose(): returns a new transposed matrix of the original matrix

get_inverse(): returns the inverse of the matrix if invertible and False otherwise

----

By default, matrix_inverter.py will ask for the user to input a matrix, and it will print the inverse of that matrix, if it is invertible.

test_matrix_inverter.py contains a test suite - this will be updated to be more extensive in the future.
