# Write your MySQL query statement below
select project_id,round(avg(experience_years),2) as average_years
from project inner join employee using(employee_id)
group by project_id;