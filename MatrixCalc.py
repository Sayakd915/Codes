import numpy as np

def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = []
    print("Enter the elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    
    return np.array(matrix)

def matrix_calculator():
    print("Matrix Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transposition")
    print("5. Determinant")
    print("6. Inversion")
    print("7. Scalar Multiplication")
    
    choice = int(input("Enter your choice (1/2/3/4/5/6/7): "))
    
    if choice in [1, 2, 3]:
        matrix1 = get_matrix()
        matrix2 = get_matrix()
        
        if choice == 1:
            result = np.add(matrix1, matrix2)
            operation = "Addition"
        elif choice == 2:
            result = np.subtract(matrix1, matrix2)
            operation = "Subtraction"
        elif choice == 3:
            result = np.dot(matrix1, matrix2)
            operation = "Multiplication"
        
        print(f"\n{operation} Result:")
        print(result)
        
    elif choice == 4:
        matrix = get_matrix()
        result = np.transpose(matrix)
        print("\nTransposition Result:")
        print(result)
        
    elif choice == 5:
        matrix = get_matrix()
        det = np.linalg.det(matrix)
        print(f"\nDeterminant Result: {det}")
        
    elif choice == 6:
        matrix = get_matrix()
        try:
            inv = np.linalg.inv(matrix)
            print("\nInverse Result:")
            print(inv)
        except np.linalg.LinAlgError:
            print("The matrix is not invertible.")
        
    elif choice == 7:
        matrix = get_matrix()
        scalar = float(input("Enter the scalar value: "))
        result = scalar * matrix
        print("\nScalar Multiplication Result:")
        print(result)
        
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    matrix_calculator()
