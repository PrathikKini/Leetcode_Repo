# Write your MySQL query statement below
with purchase as (
select customer_id, sum(case when transaction_type = 'purchase' then 1 end) as purchase_type,
coalesce(sum(case when transaction_type = 'refund' then 1 end),0) as refund_type,
count(transaction_id) as count_transactions,
datediff(max(transaction_date),min(transaction_date)) as date_diff,
(coalesce(sum(case when transaction_type = 'refund' then 1 end),0) / count(transaction_id)) * 100 as refund_rate
from customer_transactions
group by customer_id
having count_transactions > 2
and refund_rate < 20
and date_diff > 30
)

select customer_id from purchase
order by customer_id