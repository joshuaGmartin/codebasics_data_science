import numpy as np

# # py list
# n = [6, 7, 8]
# print(n[0:2])
# print(n[-1])

# # np array
# a = np.array([6, 7, 8])
# print(a[0:2])  # same
# print(a[-1])  # same

# =============================================

# a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
# print(a)
# print("============")
# # print(a[1, 2])  # 2nd row, 3rd col
# # print(a[0:2, 2])  # end is non-inclusive
# # print(a[-1])  # last row
# # print(a[-1, 0:2])
# print(a[:, 1:3])  # all rows, last two col

# =============================================

# a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
# print(a)
# print("============")
# # for row in a:
# #     print(row)  # cycles rows
# # for cell in a.flat: # as if 1D
# #     print(cell)

# =============================================

# a = np.arange(6).reshape(3, 2)
# b = np.arange(6, 12).reshape(3, 2)
# print(a)
# print("============")
# print(b)
# print("============")
# # stack
# print(np.vstack((a, b)))
# print("============")
# print(np.hstack((a, b)))

# =============================================

# a = np.arange(30).reshape(2, 15)
# print(a)
# print("============")
# # split
# b, c, d = np.hsplit(a, 3)  # (array, partitions)
# print(b)
# print("============")
# print(c)
# print("============")
# print(d)
# print("============")

# b, c = np.vsplit(a, 2)
# print(b)
# print("============")
# print(c)
# print("============")

# =============================================

# bool
a = np.arange(12).reshape(3, 4)
print(a)
print("============")
b = a > 4
print(b)
print("============")
print(a[b])  # only includes true
print("============")
a[b] = -1  # sets true to -1
print(a)
print("============")
