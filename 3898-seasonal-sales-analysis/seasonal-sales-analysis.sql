# Write your MySQL query statement below
with season_cte as (
    select case when month(sale_date) in (1,2,12) then 'Winter'
    when month(sale_date) in (3,4,5) then 'Spring'
    when month(sale_date) in (6,7,8) then 'Summer'
    when month(sale_date) in (9,10,11) then 'Fall' end as season,
    sum(quantity) as total_quantity, sum(quantity * price) as total_revenue, category
    from sales s 
     join products p
    on s.product_id = p.product_id
    group by season, category
    order by season
),
ranking as (
select season, category, total_quantity, total_revenue,
rank() over (partition by season order by total_quantity desc,total_revenue desc) as rk
from season_cte
group by season, category
)
select season, category, total_quantity, total_revenue 
from ranking
where rk = 1

