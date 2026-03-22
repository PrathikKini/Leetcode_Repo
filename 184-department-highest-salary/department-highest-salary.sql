/* Write your T-SQL query statement below */
with cte as (
select 
d.name as Department, e.name as Employee, Salary, rank() over (partition by departmentId order by salary desc) as rk
from Employee e
join Department d
on e.departmentId = d.id
)
select Department, Employee, Salary
from cte where rk = 1

