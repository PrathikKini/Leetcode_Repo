/* Write your T-SQL query statement below */
with Ranked as (
select 
student_id, subject,
first_value(score) over (partition by student_id, subject order by exam_date) as first_score,
first_value(score) over (partition by student_id, subject order by exam_date desc) as latest_score
from Scores
)
select distinct student_id, subject, first_score, latest_score
from Ranked
where latest_score > first_score
