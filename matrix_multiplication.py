
A = [
  [62, -37, -49, 18, -53, 14, 51],
  [62, -52, -11, -21, -62, -44, -95],
  [20, 78, -29, -49, -17, 21, 83],
  [-99, -69, -39, -47, 19, -50, -90],
  [91, -96, 63, -23, 5, 94, 49],
  [17, 1, 16, 63, -78, -13, -100],
  [-7, 72, 16, 86, -53, 94, 85],
  [-82, 78, 96, -45, -42, 38, 34],
  [-88, 37, 12, 31, -91, 51, 23]
]
B = [
  [90, 68, 2, 54, -59],
  [78, -86, 8, -30, 24],
  [-92, 84, -62, 13, 2],
  [12, -73, -53, -91, -4],
  [74, 85, -51, -4, 37],
  [-30, -27, 10, -78, 29],
  [-96, 39, -42, 93, 78]
]
Z = [[0 for i in range(len(B[0]))] for i in range(len(A))]
print(Z)

sum = 0
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            sum = sum + A[i][k]*B[k][j]
            Z[i][j] = sum
        sum = 0
print(Z)

#End of the program