# Write your MySQL query statement below
select product_name,year,price 
from sales A left join product B on A.product_id=B.product_id;