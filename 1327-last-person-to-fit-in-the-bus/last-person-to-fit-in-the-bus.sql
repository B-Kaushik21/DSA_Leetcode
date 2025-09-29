# Write your MySQL query statement below
select person_name 
from (
    select person_name,
    sum(weight) over(order by turn) as overall_weight
    from Queue
    order by turn
)Queue
where overall_weight<=1000
order by overall_weight desc
limit 1;
