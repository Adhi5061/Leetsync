# Write your MySQL query statement below
select id from weather A 
where A.temperature>(select temperature from weather B
where B.recordDate=A.recordDate-INTERVAL 1 DAY);