# Write your MySQL query statement below
with borrow_cte as (
select book_id, count(*) as current_borrow
from borrowing_records
where return_date is null
group by book_id
),
library_books_cte as (
    select * from library_books
)
select lb.book_id,title, author,genre, publication_year, total_copies as current_borrowers
from library_books_cte lb
join borrow_cte be
on lb.book_id = be.book_id
where total_copies - current_borrow = 0 
order by current_borrowers desc, title asc