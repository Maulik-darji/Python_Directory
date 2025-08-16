# Stirling numbers of the second kind (S(n, k))

n = int(input("Enter n (total elements): "))
k = int(input("Enter k (number of groups): "))

# Create a 2D table (matrix) for DP
S = [[0 for _ in range(k+1)] for _ in range(n+1)]

# Base cases
S[0][0] = 1

# Fill the table using recurrence
for i in range(1, n+1):
    for j in range(1, k+1):
        S[i][j] = j * S[i-1][j] + S[i-1][j-1]

print(f"Stirling Number S({n},{k}) = {S[n][k]}")

# Print full table if you want to see all values
print("\nStirling Number Table (Second Kind):")
for i in range(n+1):
    print(S[i])
