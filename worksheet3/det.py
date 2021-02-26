# det.py

def determinant(M):
    """Compute the determinant of a square matrix M

    The input matrix should be given as a list of lists.

    >>> M = [[1, 2], [3, 4]]
    >>> determinant(M)
    -2
    """
    # M is an NxN matrix
    N = len(M)

    if N == 0:
        return 1
    elif N == 1:
        return M[0][0]
    elif N == 2:
        # Handle 2x2 as the base case
        [[a, b], [c, d]] = M
        return a*d - b*c
    else:
        # Recurse using Laplace expansion for 3x3 or larger
        det = 0
        for j in range(N):
            det += (-1)**j * M[0][j] * determinant(minor(M, 0, j))
        return det


def minor(M, i, j):
    """Get the (i, j) minor of the matrix M

    The (i, j) minor of M is the matrix formed by removing the ith row and jth
    column from M.

    >>> minor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 1)
    [[4, 6], [7, 9]]
    """
    # Remove the ith row and jth column
    return [Mi[:j] + Mi[j+1:] for Mi in M[:i] + M[i+1:]]


def test_determinant():
    assert determinant([]) == 1
    assert determinant([[2]]) == 2
    assert determinant([[1, 2], [3, 4]]) == -2
    assert determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0
    assert determinant([[1, 2, 3], [4, 5, 6], [7, 8, 10]]) == -3

def test_minor():
    assert minor([], 1, 2) == []
    assert minor([[1]], 0, 0) == []
    assert minor([[1]], 1, 2) == [[1]]
    assert minor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 1) == [[4, 6], [7, 9]]