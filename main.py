import numpy as np

a = np.array([1, 2, 3], dtype="int32")
print(a)

b = np.array([[1.0, 1.3, 2.5], [1.0, 2.0, 3.0]])
print(b)

# Get Dimension
print(a.ndim)
print(b.ndim)

# Get shape

print(a.shape)
print(b.shape)

# Get Type

print(a.dtype)
print(b.dtype)

# Get Size

print(f"How many bytes are used: {a.itemsize}")
print(f"How many bytes are used: {b.itemsize}")

# Get total Size

print(f"Get total size: {a.size * a.itemsize} or {a.nbytes}")
print(f"Get total size: {b.size * b.itemsize} or {b.nbytes}")