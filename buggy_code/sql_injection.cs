using System;
using System.Data;
using System.Data.SqlClient;

namespace SqlInjectionDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get the user input
            Console.WriteLine("Enter the product name:");
            string productName = Console.ReadLine();

            // Connect to the database
            string connectionString = "Data Source=localhost;Initial Catalog=Products;Integrated Security=True";
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();

                // Build the SQL query using string concatenation
                string sql = "SELECT * FROM Products WHERE Name = '" + productName + "'";

                // Execute the query and display the results
                using (SqlCommand command = new SqlCommand(sql, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        if (reader.HasRows)
                        {
                            Console.WriteLine("Product details:");
                            while (reader.Read())
                            {
                                Console.WriteLine("ID: {0}, Name: {1}, Price: {2}", reader["ID"], reader["Name"], reader["Price"]);
                            }
                        }
                        else
                        {
                            Console.WriteLine("No product found with that name.");
                        }
                    }
                }
            }
        }
    }
}
