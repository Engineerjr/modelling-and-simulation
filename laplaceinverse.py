import sympy as sp

# Define the symbols
s = sp.symbols('s')
t = sp.symbols('t', positive=True)

# Define the new function Y(s)
Y_s = (2 * s) / ((s + 1)**2 * (s + 2))

# Display the partial fraction decomposition 
# (Highly recommended here due to the repeated root at s = -1)
partial_fractions = sp.apart(Y_s)
print("Partial Fraction Decomposition:")
print(partial_fractions)
print("-" * 40)

# Calculate the inverse Laplace transform
y_t = sp.inverse_laplace_transform(Y_s, s, t)

# Print the final result in a clean, readable format
print("Inverse Laplace Transform y(t):")
sp.pprint(y_t)