---
layout: post
title: France Boissons Relational Database with SQL
date: 2019-12-24
tags: data-analytics
image: /assets/bev.jpg
---

### Overview
France Boissons is a study case company, having the same name as the beverage distributing company in France. As a group of six, we built a operational relational database for France Boissons and wrote the most common queries for them. Our team use Oracle SQL to generate tables and queries.

<figure align="center">
	<img align="center" src="/assets/diagram.PNG" width= "600" >
	<figcaption> 
  		EER Diagram
	</figcaption>
</figure>

This is the EER (Enhanced Entity Relationship) Diagram of France Boissons. It summarizes the tables in the database and the relationship between them. The symbols at the two ends of the lines show the type of relationship. For example, let's look at the relationship between Product and Inventory. The arrows indicates inventory record contains only one products, and a product belong to at least one inventory. The EER Diagram helps employees and managers understand the database at a high level.

### Database
Our database consists of 11 tables. Each table contains a primary key. Some tables contains one or more foreign key. Primary key is the field to seperate between instances in one table, and foreign key of a table is the primary key of another one. All the tables are formulated with the purpose of simulate a real life operational database with highly simple structure. We have common tables like Customers, Orders, Inventory, and more complex one like Inventory and Shipping, with many foreign keys. We used Oracle SQL to generate the tables and populate data.

The common syntax to populate a table and its data look like this:
<pre>
# create Customer Table
create table customerT
(customerID     number(11,0)    not null,
customername    varchar2(25)    not null,
customeraddress varchar2(50)    ,
customerphone   varchar2(15)    ,
customeremail   varchar2(50)    ,
customercity   varchar(10)      ,
customercountry varchar2(20)    ,
customerzipcode varchar2(10)    ,
CONSTRAINT Customer_PK PRIMARY KEY (customerID));

#3 rows of data
insert into customerT (customerID, customername, customeraddress, customerphone, customeremail, customercity, customercountry, customerzipcode) values (120000001, 'Mon Petite Café', '33684 Tennyson Drive', '8636314376', 'lwallege0@mozilla.com', 'Nice', 'France', 65061);
insert into customerT (customerID, customername, customeraddress, customerphone, customeremail, customercity, customercountry, customerzipcode) values (120000002, 'Le Cinq', '14736 Troy Junction', '2403219237', 'drawdall1@homestead.com', 'Paris', 'France', 75006);
insert into customerT (customerID, customername, customeraddress, customerphone, customeremail, customercity, customercountry, customerzipcode) values (120000003, 'L Unic Bar', '64 Lien Alley', '3167427266', 'gdevereux2@goo.gl', 'Paris', 'France', 75001);
</pre>

We populate each table with at least 20 rows of data. If you can't tell, populating data is the most lengthy task in this project :D.

### Queries
After having the tables set up, we came up with some often used few queries that benefits the business. These queries are SQL codes allowing extract and load columns from different tables. Here are some few of them

1. Count the number of products sold for each category
<pre>
select SUM(orderlinet.orderlinequantity), productt.producttype
from orderlinet inner join productt
  on orderlinet.productid = productt.productid 
  group by productt.producttype;
</pre>

2. All Products with inventory less than 500 in all centers
<pre>
drop view Low_Quantity;
Create View Low_Quantity as
select inventoryt.productid, productt.productname,inventoryt.inventoryquantity, centerlocation, distcentert.centerid 
from inventoryt inner join productt on inventoryt.productid = productt.productid
            inner join distcentert on inventoryt.centerid = distcentert.centerid   
           where inventoryquantity <500 ; 
select * from Low_Quantity;
</pre>

3. Most quantities purchased from a customer
<pre>
Drop view QuantityPurchase;

#create view quantitiy purchase to see all customers and orders
Create view QuantityPurchase as
Select cust.customerID, cust.customername,orderT.orderID, prod.productID, prod.productname,prod.productdescription, staff.staffID, staff.staffname, orderlineT.orderlineID, orderlineT.orderlinequantity quantity
From customerT cust inner join orderT  on cust.customerID = orderT.customerID
Inner join orderlineT on orderT.orderID = orderlineT.orderID
Inner join productT prod on orderlineT.productID = prod.productID
Inner join staffT staff on orderT.staffID = staff.staffID;

#find max quantity purchase
select max(customername)as customername, max(productid) as productid, max(productname) as productname, max(quantity) MaxQuantityPurchased
from AllPurchases
group by customername;

</pre>

4. Assemble all information necessary to create an invoice for order number 10000010
<pre>
Select CustomerT.CustomerID, CustomerName, CustomerAddress,
   Ordert.OrderID, OrderDate, OrderLineT.OrderlineQuantity, 
   ProductT.ProductDescription, ProductT.productunitprice,
   (Orderlinet.OrderlineQuantity*ProductT.ProductunitPrice) Subtotalprice
From CustomerT, OrderT, OrderLineT, ProductT
where OrderT.CustomerID = CustomerT.CustomerID
and OrderT.OrderID = OrderlineT.OrderID
and OrderLineT.ProductID = ProductT.ProductID
and OrderT.OrderID = 10000010;
</pre>

5. Usual Product List: Most frequent items bought by a customer and the staff who sold them.
<pre>
# all puchases
Drop view AllPurchases;

Create view AllPurchases as
Select cust.customerID, cust.customername,orderT.orderID, prod.productID, prod.productname,prod.productdescription, staff.staffID, staff.staffname, 
        orderlineT.orderlineID, orderlineT.orderlinequantity quantity
From customerT cust inner join orderT  on cust.customerID = orderT.customerID
	Inner join orderlineT on orderT.orderID = orderlineT.orderID
	Inner join productT prod on orderlineT.productID = prod.productID
	Inner join staffT staff on orderT.staffID = staff.staffID;

# usual product list
select max(customername)as customername, max(productid) as productid, max(productname) as productname,max(productdescription) as productdescription, max(staffID)as staffID, max(staffname) as salesman, count(productid) TimePurchased, round(avg(quantity),0) AverageQuantityPurchased
from AllPurchases
group by customername
having count(productid) > 2;
</pre>

### Advantages and Limits
Following is some reflection on this project
●	Our project is simple, the architecture is quite common, but the big advantage is that it remains applicable for other businesses as well.
●	We have chosen to be very precise about the naming convention so that it is easy to understand the tables and also very easy to retrieve data and build queries.
●	Data structure ensures business efficiency. Our advantage here is about the Usual Product List that helps sales man to have a better understanding of their customer preferences.
However, we have a room for improvement:
●	Our database is not integrated, which is complicated because when we will change something in a table the information will not be updated if it appears in another table.
●	It is also complicated to restructure primary keys, before we would have to make sure about where it appears, because it is not integrated.

