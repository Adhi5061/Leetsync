# Write your MySQL query statement below
-- select customer_id,count(customer_id) count_no_trans from visits left join transactions using(visit_id)
-- where transaction_id is NULL group by customer_id order by count_no_trans; 

select customer_id,count(customer_id) as count_no_trans from visits
where visit_id not in (select visit_id from transactions) 
group by customer_id;