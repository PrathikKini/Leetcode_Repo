select b.book_id, title, author, genre, pages,
max(r.session_rating) - min(r.session_rating) as rating_spread,
round(sum(case when r.session_rating <=2 or r.session_rating >=4 then 1 else 0 end) * 1.0 / count(*),2) as polarization_score
from books b 
join reading_sessions r
on b.book_id = r.book_id
group by b.book_id, title, author, genre, pages
having count(*) >= 5
and min(r.session_rating) <= 2
and max(r.session_rating) >= 4
and round(sum(case when r.session_rating <=2 or r.session_rating >=4 then 1 else 0 end) * 1.0 / count(*) >= 0.6,2)
order by polarization_score desc, title desc
