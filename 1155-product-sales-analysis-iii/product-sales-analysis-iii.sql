/* Write your T-SQL query statement below */
select product_id, year as first_year, quantity, price
from
(
    select *, rank() over (partition by product_id order by year) rn
    from Sales
) t
where rn = 1