# Write your MySQL query statement below
with positive as (
    select min(test_date) as min_pos_date, patient_id
    from covid_tests
    where result = 'Positive'
    group by patient_id
),
negative as (
    select min(test_date) as min_neg_date, p.patient_id
    from covid_tests c
    join positive p
    on p.patient_id = c.patient_id
    and c.test_date > p.min_pos_date
    where result = 'Negative'
    group by patient_id
)
select p.patient_id, patient_name, age, datediff(min_neg_date,min_pos_date) as recovery_time
from positive p 
join negative n
on p.patient_id = n.patient_id
join patients pt
on pt.patient_id = p.patient_id
order by recovery_time, patient_name