import numpy 

# Create numpy arrays (Vectors)
array_a = numpy.array([4, 5, 10, 22, 12, 3, 100])
array_b = numpy.array([1, 2, 1, 5, 11, 55, 88])

# SCALAR ARITHMETIC OPERATIONS (Element-wise)
# A scalar value is applied to every element of the array.

# Scalar addition
r = array_a + 10
print(f"Resultado da adição escalar: {r}\n")

# Scalar subtraction 
r = array_a - 10
print(f"Resultado da subtração escalar: {r}\n")

# Scalar multiplication 
r = array_a * 2
print(f"Resultado da multiplicação escalar: {r}\n")

# Scalar division 
r = array_a / 2
print(f"Resultado da divisão escalar: {r}\n")

# VECTOR ARITHMETIC OPERATIONS (Element-wise)
# These are linear operations applied element by element.
# IMPORTANT: Both arrays MUST have the same dimension (shape).

# Vector addition
r = array_a + array_b
print(f"Resultado da adição vetorial: {r}\n")

# Vector subtraction
r = array_a - array_b
print(f"Resultado da subtração vetorial: {r}\n")

# Vector multiplication (Element-wise)
# This is NOT the dot product; it multiplies elements at the same index.
r = array_a * array_b
print(f"Resultado da multiplicação vetorial (elemento a elemento): {r}\n")

# Vector division (Element-wise)
r = array_a / array_b
print(f"Resultado da divisão vetorial (elemento a elemento): {r}\n")

# DOT PRODUCT
# The dot product is the sum of the element-wise products.
# It results in a single scalar value.
r = numpy.dot(array_a, array_b)
print(f"Produto Escalar (Dot Product): {r}")