--1
select  productname,  price
from products
where catid = 1 
order by price desc
LIMIT 3
--2
SELECT productname, name as CategoryName”, price 
FROM products, cat
where catid =  id
--3
ALTER TABLE products
ADD Description varchar(50);
--4
UPDATE products
SET
Description =(select productName || "_Desc" as des)
--5
UPDATE products
SET
price =30
where productname = "laundry detergent"


