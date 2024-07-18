# Write your MySQL query statement below
select A1.machine_id,round(avg(A2.timestamp-A1.timestamp),3) as processing_time from Activity A1 
inner join Activity A2
on A1.machine_id=A2.machine_id and A1.process_id=
A2.process_id and A1.timestamp<A2.timestamp
 group by machine_id;
