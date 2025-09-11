# Write your MySQL query statement below
with process as 
(
    select employee_id, sum(duration_hours) as total_sum
    from meetings
    group by employee_id, weekofyear(meeting_date), year(meeting_date)
)
select e.employee_id, employee_name, department, 
count(e.employee_id) as meeting_heavy_weeks
from process p
join employees e
on p.employee_id = e.employee_id
where total_sum > 20
group by e.employee_id, employee_name, department
having meeting_heavy_weeks > 1
order by meeting_heavy_weeks desc, employee_name