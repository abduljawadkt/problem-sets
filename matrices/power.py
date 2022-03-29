def zero_matrix(n): 
 '''zero matrix of size n x n''' 
 M = [ ] 
 for i in range(n): 
 row = [ ] 
 for j in range(n): 
row.append(0) 
M.append(row) 
 return M 
def mat_mul(A, B): 
 '''multiply A and B''' 
 n = len(A) 
 prod = zero_matrix(n) 
 # multiply A and B 
 for i in range(n): 
 for j in range(n): 
for k in range(n): 
 prod[i][j] += A[i][k] * B[k][j] 
 return prod 
def power(A, m): 
 '''Raise A to the power m''' 
 if m == 1: 
 return A 
A_min_one = power(A, m - 1) 
 return mat_mul(A_min_one, A) 