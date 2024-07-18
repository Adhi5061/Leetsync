# Write your MySQL query statement below
select contest_id,round(count(user_id)/(select count(distinct user_id) from users )*100,2)  as percentage 
from users A inner join  register
using (user_id) group by contest_id
order by percentage desc, contest_id;