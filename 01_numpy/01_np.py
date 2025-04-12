import numpy as np

# a = np.array([5, 6, 9])

# print(a[0])
# print(a[1])
# print(a.ndim)
# print(a.shape)

# ===============================================

# a = np.array(
#     [
#         [1, 2],
#         [3, 4],
#         [5, 6],
#     ],
#     # dtype=np.int32,
#     # dtype=np.float64,
#     dtype=complex,
# )
# print(a)
# print(a.dtype)
# print(a.ndim)
# print(a.shape)
# print(a.itemsize)

# ===============================================

# a = np.array(
#     [
#         [1, 2],
#         [3, 4],
#         [5, 6],
#     ],
# )

# print(a.size)
# print(a.shape)

# ===============================================

# # a = np.zeros((3, 4))
# # a = np.ones((3, 4))
# # print(a)

# l = range(5)
# print(l)
# print(l[1])

# # a = np.arange(1, 5)
# # a = np.arange(1, 5, 2) # start 1, step 2, stop when reach 5
# # a = np.linspace(1, 5, 10)  # 10 linearly spaced number between 1 and 5
# a = np.linspace(1, 10, 10)
# print(a)

# ===============================================

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)
# print(a.shape)

# print("============")

# # must use a = a.method() to update orginal array
# a = a.reshape(2, 3)
# print(a)
# print(a.shape)

# print("============")

# a = a.reshape(6, 1)
# print(a)
# print(a.shape)

# print("============")

# a = a.ravel()  # flatten to one row (1D)
# print(a)
# print(a.shape)

# ===============================================

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a)
# print(a.min())
# print(a.max())
# print(a.sum())
# print(a.sum(axis=0))  # sum vertical (axis0)
# print(a.sum(axis=1))  # sum horizontal (axis1)

# print(np.sqrt(a))
# print(np.std(a))
# print(np.mean(a))

# ===============================================

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a)
print("============")
print(b)
print("============")
print(a + b)
print("============")
print(a / b)
print("============")
print(a * b)
print("============")
print(a.dot(b))  # matrix product
