# Write your MySQL query statement below
select A.product_id,coalesce(round(sum(price*units)/sum(units),2),0) as average_price from
prices A left join unitsSold B
on A.product_id=B.product_id and B.purchase_date>=A.start_date
and B.purchase_date<=A.end_date group by A.product_id;