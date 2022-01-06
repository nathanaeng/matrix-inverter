import unittest
from matrix_inverter import Matrix

class TestMatrixConstructor(unittest.TestCase):

    def test_invalid_matrix(self):
        data = [[0,4,3],[0,0]]
        with self.assertRaises(Exception):
             m = Matrix(data)
        self.assertTrue("Invalid matrix. Each row must have an equal length.")

    def test_size(self):
        data = [[0,4,3],[0,0,4],[1,2,3], [0,0,1]]
        m = Matrix(data)
        self.assertEqual([4,3], m.size)


class TestDeterminant(unittest.TestCase):

    def test_get_det_3x3(self):
        data = [[0,4,3],[0,0,4],[1,2,3]]
        m = Matrix(data)
        self.assertEqual(16, m.get_det())

        data = [[-12,5,0],[1,7,1],[2,2,0]]
        m = Matrix(data)
        self.assertEqual(34, m.get_det())

        data = [[1,1,-2],[1,-2,1],[-2,1,1]]
        m = Matrix(data)
        self.assertEqual(0, m.get_det())

    def test_get_det_expand_2nd_row(self):
        data = [[0,4,3],[0,0,4],[1,2,3]]
        m = Matrix(data)
        self.assertEqual(16, m.get_det(row=2))

    def test_has_inverse(self):
        data = [[0,4,3],[0,0,4],[1,2,3]]
        m = Matrix(data)
        self.assertEqual(True, m.has_inverse())

        data = [[1,1,-2],[1,-2,1],[-2,1,1]]
        m = Matrix(data)
        self.assertEqual(False, m.has_inverse())


class TestTranspose(unittest.TestCase):

    def test_transpose_3x3(self):
        data = [[0,4,3],[0,0,4],[1,2,3]]
        m = Matrix(data)
        transposed = [[0,0,1],[4,0,2],[3,4,3]]
        self.assertEqual(transposed, m.transpose().data)


class TestInverse(unittest.TestCase):

    def test_inverse_3x3(self):
        data = [[0,3,1],[2,0,0],[1,-2,1]]
        m = Matrix(data)
        inverse_m = [[0, 0.5, 0], [0.2, 0.1, -0.2], [0.4, -.3, 0.6]]
        self.assertEqual(inverse_m, m.get_inverse().data)


if __name__ == '__main__':
    unittest.main()