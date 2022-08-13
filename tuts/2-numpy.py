# ## CONCEPT
# * the core of numpy is `ndarray` object
#   * ndarray is a multi-dimensional array

import numpy as np

# * array is fixed-size, homogeneous data container
#   * must be same type
#   * more efficient

# %% numpy array

# ndarray.ndim - number of dimensions
# ndarray.shape - shape of the array (n,m) - n rows, m columns
# ndarray.size - number of elements in the array
# ndarray.dtype - data type of the array
# ndarray.itemsize - size in bytes of each element
# ndarray.data - memory address of the start of the array

a = np.arange(15).reshape(3, 5)

# check these value...
a.shape
a.ndim
a.dtype.name
a.itemsize
a.size
type(a)

# %% numpy array
a = np.array([2, 3, 4])
b = np.array([1.2, 3.5, 5.1])
b.dtype
b = np.array([(1.5, 2, 3), (4, 5, 6)])
c = np.array([[1, 2], [3, 4]], dtype=complex)

# %% create
np.zeros((3, 4))
np.ones((2, 3, 4), dtype=np.int16)
np.empty((2, 3))  # lick c array
np.arange(10, 30, 5)  # mean a-range
np.linspace(0, 2, 9)  # more precisely than arange()

# %% op
a = np.array([[1, 2], [3, 4]]).reshape(4)
b = np.arange(4)

# check these value
a + b
a * b
a ** b
10 * np.sin(a)
a < 3

# %% matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 1], [1, 0]])

A * B
A @ B  # matrix multiplication
A.dot(B)  # same, matrix multiplication

# %% more op
rg = np.random.default_rng(888)
a = rg.random((2, 3))

a.max(axis=1)
a.sum(axis=0)
a.cumsum()
a.cumsum(axis=1)
np.exp(a)
np.sqrt(a)

a = rg.random(8)
a[:8:2] = 2

a = rg.random((4, 4))
a[1:3, 1:3]
a[-1]  # reversed a

# %% type
a = np.ones(3, dtype=np.int32)
b = np.linspace(0, 1, 3)


# a += b # can't
# NOTE: numpy is strong typed, same as c/c++

# %% from function
def f(x, y):
    return 10 * x + y


a = np.fromfunction(f, (5, 4), dtype=np.int32)

# %% array indexing
c = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[3, 1, 2], [5, 4, 6]]
])

c.shape

c[1]
c[:, 1, :]

# %% iter
rg = np.random.default_rng(888)
a = rg.random((2, 4))

for row in a:
    print(row)

for i in a.flat:
    print(i)

# %% shape
a = np.floor(10 * rg.random((3, 4)))
a.flatten()
a.reshape(6, 2)
a.T  # transpose
a.reshape(6, -1)  # -1 means: the other dimensions are automatically calculated

# %% stack
a = np.floor(10 * rg.random((2, 2)))
b = np.floor(10 * rg.random((2, 2)))
np.vstack((a, b))
np.hstack((a, b))
a = np.array([1, 2])
b = np.array([3, 4])
np.column_stack((a, b))

# %% split
a = np.floor(10 * rg.random((2, 12)))
np.hsplit(a, 3)
np.hsplit(a, (3, 4))  # Split `a` after the third and the fourth column

# %% copy & view
a = np.floor(10 * rg.random((2, 12)))
c = a.view()
c.base is a  # True
c.flags.owndata  # False

d = a.copy()

a = np.arange(int(1e8))
b = a[:100]
del a  # release mem

# %% array index with index array
a = np.arange(10) ** 2
i = np.array([1, 1, 3, 8])
a[i];

j = np.array([[3, 4], [9, 7]])
a[j]

# %% array index example
palette = np.array([[0, 0, 0],  # black
                    [255, 0, 0],  # red
                    [0, 255, 0],  # green
                    [0, 0, 255],  # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])

palette[image]

# %% array index with index array 2D
a = np.arange(12).reshape(3, 4)

i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])

a[i, j]  # i and j must have equal shape
a[(i, j)]  # same as above
a[[1, 2]] = 0

# %% boolean
a = np.arange(12).reshape(3, 4)
b = a > 4

a[b]  # 1D
a[b] = 0

