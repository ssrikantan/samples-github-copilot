-- Declare variables to store the parameters
DECLARE @StartDate DATE = '2019-01-01';
DECLARE @EndDate DATE = '2019-12-31';
DECLARE @ProductCategoryName VARCHAR(50) = 'Bikes';

-- Query the SalesOrderHeader, SalesOrderDetail, Product, ProductSubcategory, and ProductCategory tables
-- Join them on the foreign key columns
-- Filter by the date range and the product category name
-- Group by the sales order number, customer name, order date, and product name
-- Calculate the total quantity and amount for each order and product
-- Order by the sales order number in descending order
SELECT 
    SOH.SalesOrderNumber AS OrderNumber,
    C.FirstName + ' ' + C.LastName AS CustomerName,
    SOH.OrderDate AS OrderDate,
    P.Name AS ProductName,
    SUM(SOD.OrderQty) AS TotalQuantity,
    SUM(SOD.LineTotal) AS TotalAmount
FROM Sales.SalesOrderHeader AS SOH
INNER JOIN Sales.SalesOrderDetail AS SOD
ON SOH.SalesOrderID = SOD.SalesOrderID
INNER JOIN Production.Product AS P
ON SOD.ProductID = P.ProductID
INNER JOIN Production.ProductSubcategory AS PS
ON P.ProductSubcategoryID = PS.ProductSubcategoryID
INNER JOIN Production.ProductCategory AS PC
ON PS.ProductCategoryID = PC.ProductCategoryID
INNER JOIN Sales.Customer AS C
ON SOH.CustomerID = C.CustomerID
WHERE SOH.OrderDate BETWEEN @StartDate AND @EndDate
AND PC.Name = @ProductCategoryName
GROUP BY SOH.SalesOrderNumber, C.FirstName + ' ' + C.LastName, SOH.OrderDate, P.Name
ORDER BY SOH.SalesOrderNumber DESC;
