import re

def read_matrixfile(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        rows, cols = map(int, lines[0].split())

        matrix = [list(line.strip()) for line in lines[1:]]
        matrix = [row + [" "] * (cols - len(row)) for row in matrix]
    
    return matrix

def process_matrix(matrix):
    transposed_matrix = list(zip(*matrix))
    decoded_string = "".join("".join(row) for row in transposed_matrix)
    
    cleaned_string = re.sub(r"(?<=\w)([^\w\d]+)(?=\w)", " ", decoded_string)
    return cleaned_string

file_name = "matriks2.txt"
matrix = read_matrixfile(file_name)

print("\nInput Matriks:\n")
for row in matrix:
    print("".join(row))

decoded_string = process_matrix(matrix)
print("\nDecode:", decoded_string)