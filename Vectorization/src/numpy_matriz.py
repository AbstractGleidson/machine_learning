import numpy

# MATRIX CREATION
# A matrix is a 2-dimensional array. Operations are performed using two coordinates: rows and columns.
# np.arange(0, 10) creates a 1D array [0, 1, ..., 9].
# .reshape(-1, 5) restructures the array into a matrix with 5 columns; -1 automatically calculates the number of rows (which is 2).
matriz = numpy.arange(0, 10, dtype=float).reshape(-1, 5)

print(f"Matriz: \n{matriz}\n")
print(f"Forma da Matriz (Shape): {matriz.shape}\n")
print(f"Tipo de Dado da Matriz (Dtype): {matriz.dtype}\n")

# SCALAR AND VECTOR OPERATIONS ON MATRIX SUBSETS
# Operations are performed by slicing the matrix to extract 1D vectors (rows or partial rows).

# 1. SCALAR ADDITION on a row (Row 0)
# Selects all columns (0:) in the first row (0) and adds the scalar value.
sum_m = matriz[0, 0:] + 1000
print(f"Resultado da adição escalar na Linha 0: {sum_m}\n")

# 2. ELEMENT-WISE MULTIPLICATION (Vector-Vector)
# Multiplies the vector from Row 0 by the vector from Row 1, element-by-element.
# Both slices must have the same shape: (5,)
produto = matriz[0, 0:] * matriz[1, 0:]
print(f"Resultado da multiplicação vetorial (Linha 0 * Linha 1): {produto}\n")

# 3. DOT PRODUCT (Vector-Vector)
# Calculates the dot product between the vector from Row 0 and the vector from Row 1.
# This results in a single scalar value.
dot = numpy.dot(matriz[0, 0:], matriz[1, 0:])
print(f"Produto Escalar (Dot Product) entre Linha 0 e Linha 1: {dot}\n")

# 4. MATRIX INDEXING (Accessing a single element)
# Accesses the element in the 1st row (index 1) and 3rd column (index 3).
elemento = matriz[1, 3]
print(f"Elemento acessado na posição [1, 3]: {elemento}\n")

# 5. MATRIX SLICING (Accessing a subset of columns across all rows)
# Selects all rows (:) and columns from index 1 up to (but not including) index 4.
sub_matriz = matriz[:, 1:4]
print(f"Sub-matriz (Todas as linhas, Colunas 1 a 3):\n{sub_matriz}\n")

# 6. AGGREGATE FUNCTION (Summing a column/axis)
# Calculates the sum of all elements in the matrix along a specific axis.
# axis=0 sums down the rows (results in a vector of column sums).
soma_colunas = numpy.sum(matriz, axis=0)
print(f"Soma dos elementos por coluna (axis=0): {soma_colunas}\n")

# 7. AGGREGATE FUNCTION (Mean/Average)
# Calculates the mean of all elements in the matrix.
media_total = numpy.mean(matriz)
print(f"Média de todos os elementos da matriz: {media_total}")