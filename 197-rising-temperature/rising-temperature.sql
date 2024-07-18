# Write your MySQL query statement below
-- select id from weather A 
-- where A.temperature>(select temperature from weather B
-- where B.recordDate=A.recordDate-INTERVAL 1 DAY);
-- select w2.id as Id from weather w1 left join 
-- weather w2 on w1.recordDate=w2.recordDate-Interval 1 day
-- where w2.temperature>w1.temperature;
select w2.id from weather w1 join weather w2
where Datediff(w2.recordDate,w1.recordDate)=1
and w2.temperature>w1.temperature;