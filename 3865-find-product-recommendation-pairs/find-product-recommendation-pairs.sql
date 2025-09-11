# Write your MySQL query statement below
select t1.product_id as product1_id, t2.product_id as product2_id, 
p1.category as product1_category, p2.category as product2_category,
count(distinct t1.user_id) as customer_count
from ProductPurchases t1
join ProductPurchases t2
on t1.user_id = t2.user_id and t1.product_id < t2.product_id
join ProductInfo p1 on p1.product_id = t1.product_id
join ProductInfo p2 on p2.product_id = t2.product_id
group by 1,2,3,4
having customer_count > 2
order by customer_count desc, t1.product_id, t2.product_id