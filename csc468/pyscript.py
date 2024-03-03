import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="172.18.0.2",     # IP address of the Docker container
    user="kush",           # MySQL username
    password="password",   # MySQL password
    database="csc468"      # MySQL database
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Example query: Select all rows from a table
query = "SELECT * FROM cattle"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()

