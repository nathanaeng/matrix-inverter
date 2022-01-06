### give the inverse of a matrix if it is invertible
class Matrix():
    
    def __init__(self, data, getDet = False) -> None:
        '''
        m x n matrix

        data: [[],[],[],[],...]
        size: m x n matrix represented as [m, n]
        '''
        if not getDet:
            length_row = len(data[0])
            for row in data:
                assert len(row) == length_row, "Invalid matrix. Each row must have an equal length."
        self.data = data

        self.size = [len(data), len(data[0])]

    def __str__(self) -> str:
        return f'{self.data}'

    def clean_str(self) -> str:
        '''returns a better visual representation of the matrix'''
        x = ''
        for m in range(len(self.data)):
            x += '['
            for n in self.data[m]:
                x += f'{n: ^10}'
            x += ']\n'
        return x

    def get_det(self, m=None, row=1, adj=False) -> int:
        '''
        return the determinant of self, if m is defined then
        return the determinant of m
        
        expand across row 1 by default
        
        if adj=True, return a list of the sub determinants
        '''
        if row > len(self.data):
            raise Exception("Must expand across a row number <= number of rows in matrix")
        if m is None:  # for first iter
            m = self
        det = 0
        subs = []

        if len(m.data) == 2 and len(m.data[0]) == 2:
            '''
            [00][01]
            [10][11]
            '''
            val = m.data[0][0] * m.data[1][1] - m.data[0][1] * m.data[1][0]
            return val

        for x in range(len(m.data)):
            new = m.data.copy()  # excludes first row
            new = new[0:row-1]+new[row:]
            height = len(new)

            for i in range(height):
                new[i] = new[i][0:x] + new[i][x+1:]  # remove corresponding col
                m_sub = Matrix(new, getDet=True)
            sub_det = self.get_det(m=m_sub)
            subs.append(sub_det)
            det += m.data[row-1][x] * (-1)**(1+x+1) * sub_det  # index starts at 1 in formula

        if adj is True:
            return subs
        if row % 2 == 0:
            det *= -1
        return det

    def has_inverse(self) -> bool:
        '''check if matrix is invertible'''
        if len(self.data)!=len(self.data[0]):
            # Not a square matrix, so not invertible
            return False

        det = self.get_det()

        if det == 0:
            return False
        else:
            return True

    def transpose(self) -> "Matrix":
        '''returns the transposed matrix'''
        new = []
        for idx in range(len(self.data)):
            temp = []
            for m in self.data:
                temp.append(m[idx])
            new.append(temp)
        m = Matrix(new)
        return m

    def get_inverse(self) -> "Matrix":
        '''
        return a new matrix which is the inverse of self
        
        calculates the cofactor matrix using Cramer's rule, then
        multiplies each value in the cofactor matrix by the reciprocal
        of the determinant, then transposes the resulting matrix.
        
        typically, you transpose the cofactor matrix first to get the
        adjugate matrix, and then multiply that by the reciprocal of the
        determinant - the order was changed to decrease the runtime

        https://en.wikipedia.org/wiki/Minor_(linear_algebra)
        https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html
        '''
        m_cofactors = []
        det = self.get_det()
        for m in range(len(self.data)):
            subs = self.get_det(row=m+1, adj=True)
            m_cofactors.append(subs)  # matrix of cofactors
            for c in range(len(subs)):
                m_cofactors[m][c] /= det  # multiply each val by reciprocal of the determinant of self
                m_cofactors[m][c] = round(m_cofactors[m][c], 5)  # only 5 decimal places
                if (m + c) % 2:  # apply "checkerboard" of negatives
                    m_cofactors[m][c] *= -1
                if m_cofactors[m][c] == -0:  # fix any "negative" 0s
                    m_cofactors[m][c] = 0
        return Matrix(m_cofactors).transpose()  # transpose to get inverse


if __name__ == "__main__":
    print("\nGiven a matrix 'A', this script will calculate the inverse of 'A' (if 'A' is invertible).\n")
    print("Enter values, separated by a ',' or a space. 'Enter' to start a new row. 'D' on a newline when done.\n")

    temp = []
    x = input()
    while(x != 'D' and x != 'd'):
        temp.append(x)
        x = input()
    
    m = []
    for s in temp:
        x = s.replace(',', ' ').replace('  ', ' ').split(' ')  # make: (1,1,1), (1 1 1), (1, 1, 1), (1,1 1), ... readable
        for i in range(len(x)):
            x[i] = int(x[i])
        m.append(x)
    a = Matrix(m)
    print(f"\nYour matrix is:\n\n{a.clean_str()}\n")
    if a.has_inverse():
        print(f"Inverse:\n{a.get_inverse().clean_str()}\n")
    else:
        print(f"Matrix is not invertible.\n")
