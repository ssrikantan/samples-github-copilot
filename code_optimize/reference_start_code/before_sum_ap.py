# Define a function that takes n as a parameter
def sum_of_first_n(n):
  # Initialize a variable to store the sum
  sum = 0
  # Loop from 1 to n
  for i in range(1, n+1):
    # Add i to the sum
    sum = sum + i
  # Return the sum
  return sum