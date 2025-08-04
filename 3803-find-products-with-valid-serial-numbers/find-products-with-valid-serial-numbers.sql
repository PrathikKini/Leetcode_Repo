# Write your MySQL query statement below
select * from products where description
collate utf8mb3_bin regexp '(^|[^A-Z0-9])SN[0-9]{4}-[0-9]{4}(?![0-9])'