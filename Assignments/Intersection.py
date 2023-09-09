# Write a Python program to find the intersection of two given arrays using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]
# Intersection of the said arrays: [1, 2, 8, 9]

# intersection attribute is only for set datatype

Array1 = {1, 2, 3, 5, 7, 8, 9, 10}
Array2 = {1, 2, 4, 8, 9}

inter = lambda x, y: x.intersection(y) ; print(inter(Array1, Array2))
