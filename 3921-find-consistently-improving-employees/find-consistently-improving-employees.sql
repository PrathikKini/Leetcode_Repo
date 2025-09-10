# Write your MySQL query statement below
with ranking as (
select pr.employee_id,name,rating,rank() over 
(
    partition by pr.employee_id order by review_date desc
) as rk
from performance_reviews pr
join employees e on
pr.employee_id = e.employee_id
),
pivoting as (
    select employee_id, name,
    max(case when rk = 1 then rating end) as latest_rating,
    max(case when rk = 2 then rating end) as second_rating,
    max(case when rk = 3 then rating end) as third_rating
    from ranking
    group by employee_id, name
)
select employee_id, name, latest_rating - third_rating as improvement_score
from pivoting
where latest_rating is not null
and second_rating is not null
and third_rating is not null
and latest_rating > second_rating and second_rating > third_rating
and latest_rating > third_rating
order by improvement_score desc, name asc
