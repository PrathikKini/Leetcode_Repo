# Write your MySQL query statement below
with trial as (
select user_id, round(avg(activity_duration),2) as trial_avg_duration
from UserActivity
where activity_type = 'free_trial'
group by user_id
),
paid as (
select user_id, round(avg(activity_duration),2) as paid_avg_duration
from UserActivity
where activity_type = 'paid'
group by user_id
)
select t.user_id, trial_avg_duration, paid_avg_duration
from trial t
join paid p
on t.user_id = p.user_id