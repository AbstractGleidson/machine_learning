import numpy 

# Creating array numpy
array_zero = numpy.zeros(10, dtype=float) # creates a zero-filled array of float type
print(f"Array zero: {array_zero}\nArray shape: {array_zero.shape}\nArray type: {array_zero.dtype}\n\n")
# array.shape : Dimensions of array in rows and colunms 
# array.dtype : Type of array

array_arange = numpy.arange(0, 10, 2, dtype=int) # Create filled array with values in intervale [start, stop - 1, step] 
print(f"Array arange: {array_arange}\nArray shape: {array_arange.shape}\nArray type: {array_arange.dtype}\n\n")

array_random_sample = numpy.random.random_sample(10) # Create filled array with values in intervale [0.0, 1.0]
print(f"Array aleatorio simples: {array_random_sample}\nArray shape: {array_random_sample.shape}\nArray type: {array_random_sample.dtype}\n\n")

array_random = numpy.random.rand(10) # Create fillend array with values in intervale [0.0, 1.0] uniforme
print(f"Array aleatorio simples: {array_random}\nArray shape: {array_random.shape}\nArray type: {array_random.dtype}\n\n")

array_values = numpy.array([1, 2, 3, 4, 5, 6, 7], dtype=int)# Create filled array with values pass for list 
print(f"Array aleatorio simples: {array_values}\nArray shape: {array_values.shape}\nArray type: {array_values.dtype}\n\n")