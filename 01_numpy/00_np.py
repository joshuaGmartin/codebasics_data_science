import numpy as np
import sys
import time

# a = np.array([1, 2, 3])
# print(a)
# print(a[0])
# print(a[1])

# # arrays save mem
# l = range(1000)
# print(sys.getsizeof(5) * len(l))

# array = np.arange(1000)
# print(array.size * array.itemsize)

# ==============================================

# # arrays save time
# SIZE = 1000000
# l1 = range(SIZE)
# l2 = range(SIZE)

# a1 = np.arange(SIZE)
# a2 = np.arange(SIZE)

# # py list
# start = time.time()
# result = [(x + y) for x, y in zip(l1, l2)]
# l_time = (time.time() - start) * 1000
# print("list time:", time)

# # np array
# start = time.time()
# result = a1 + a2  # no list comprehension needed
# a_time = (time.time() - start) * 1000
# print("array time:", time)

# print("np times faster:", l_time / a_time)

# ==============================================

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
