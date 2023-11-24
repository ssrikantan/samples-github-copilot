# Import the modules
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("example.db")

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Get the user input for the query parameters
print("Enter the table name:")
table_name = input()
print("Enter the column name:")
column_name = input()
print("Enter the value to filter by:")
value = input()

# Build the SQL query using string formatting
sql = "SELECT * FROM {} WHERE {} = ?".format(table_name, column_name)

# Execute the query and fetch the results
cur.execute(sql, (value,))
results = cur.fetchall()

# Convert the results to a pandas dataframe
df = pd.DataFrame(results, columns=[col[0] for col in cur.description])

# Display the dataframe
print(df)

# Close the cursor and the connection
cur.close()
conn.close()
