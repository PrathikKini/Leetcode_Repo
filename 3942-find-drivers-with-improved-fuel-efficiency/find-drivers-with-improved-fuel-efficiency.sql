with trip_efficiency as
(
    select driver_id,
    case when month(trip_date) between 1 and 6 then 'first' else 'second' end as half, 
    distance_km / fuel_consumed as fuel_efficiency
    from trips
),
first_half_cte as (
select driver_id,
avg(fuel_efficiency) as first_half
from trip_efficiency
where half = 'first'
group by driver_id
),
second_half_cte as (
select driver_id,
avg(fuel_efficiency) as second_half
from trip_efficiency
where half = 'second'
group by driver_id
)
select f.driver_id, driver_name, round(first_half,2) as first_half_avg, round(second_half,2) as second_half_avg, 
round(second_half - first_half,2) as efficiency_improvement
from first_half_cte f join second_half_cte s
on f.driver_id = s.driver_id
join drivers d on d.driver_id = f.driver_id
where round(second_half - first_half,2) > 0
order by efficiency_improvement desc, driver_name 
