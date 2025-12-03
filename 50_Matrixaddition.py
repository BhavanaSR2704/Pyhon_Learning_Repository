# Take number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input first matrix
print("Enter elements of Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input(f"A[{i}][{j}] = "))
        row.append(x)
    A.append(row)

# Input second matrix
print("Enter elements of Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input(f"B[{i}][{j}] = "))
        row.append(x)
    B.append(row)

# Add matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)

# Display result
print("Resultant Matrix after addition:")
for r in result:
    print(r)


#==============================O/P:-
Enter number of rows: 2
Enter number of columns: 2
Enter elements of Matrix A:
A[0][0] = 2
A[0][1] = 2
A[1][0] = 2
A[1][1] = 2
Enter elements of Matrix B:
B[0][0] = 3
B[0][1] = 3
B[1][0] = 3
B[1][1] = 3
Resultant Matrix after addition:
[5, 5]
[5, 5]
