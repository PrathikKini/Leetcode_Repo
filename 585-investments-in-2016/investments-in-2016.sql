/* Write your T-SQL query statement below */
select 
round(sum(tiv_2016),2) as tiv_2016
from Insurance t1
where tiv_2015 in
(
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*) > 1
)
and not exists
(
    select 1
    from Insurance t2
    where t1.pid != t2.pid
    and t1.lat = t2.lat
    and t1.lon = t2.lon
)