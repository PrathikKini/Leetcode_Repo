# Write your MySQL query statement below
select customer_id, count(1) as total_orders,
round((sum(case when (time(order_timestamp) between '11:00:00' and '14:00:00') or (time(order_timestamp) between '18:00:00' and '21:00:00') then 1 else 0 end) / count(1) * 100)) as peak_hour_percentage,
round(avg(order_rating),2) as average_rating
from restaurant_orders 
group by customer_id 
having avg(order_rating) >= 4 
and (count(order_rating) / count(1)) * 100 >= 50
and peak_hour_percentage >= 60
and total_orders > 2
order by average_rating desc, customer_id desc