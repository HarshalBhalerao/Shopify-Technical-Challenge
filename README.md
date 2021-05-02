# Shopify-Technical-Challenge

## Question 1
Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

- Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
- What metric would you report for this dataset?
- What is its value?

### Solution:
- Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.
  - Average order value(AOV) is calculated as total sales divided by the order count
  - In the calculations above we have total sales divided by the count. To get the right solution we need to sum up all the orders and then use that as our order count.
  - Formula: AOV = total sales / order Count 

- What metric would you report for this dataset?
  - Use the formula above
  - Total sales will be the sum of all the order amounts.
  - And order count will be the sum of all the total items.

- What is its value?
  - The answer that I get from this is 357.92152221412965 dollars

Link to the [code](https://github.com/HarshalBhalerao/Shopify-Technical-Challenge/blob/main/solution1.py)


## Question 2: 
For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

- How many orders were shipped by Speedy Express in total?
  - Query: 
     ``` SELECT count(*) FROM Orders JOIN Shippers ON Shippers.ShipperID=Orders.ShipperID where Shippers.ShipperName = "Speedy Express"; ```
  - Answer: 54
- What is the last name of the employee with the most orders?
  -  Query: 
      ``` SELECT Employees.LastName, count(*) FROM Orders JOIN Employees ON Employees.EmployeeID=Orders.EmployeeID GROUP BY LastName ORDER BY COUNT(*) desc limit 1; ```
  -  Answer: Peacock  40
- What product was ordered the most by customers in Germany?
  - Query: 
    ``` SELECT Products.ProductName, OrderDetails.Quantity FROM Orders, OrderDetails JOIN Customers ON Orders.CustomerID=Customers.CustomerID JOIN Products ON OrderDetails.ProductID=Products.ProductID WHERE Country='Germany' ORDER BY OrderDetails.Quantity desc limit 1; ```
  - Answer: Pâté chinois 120
