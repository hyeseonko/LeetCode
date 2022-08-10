# Write your MySQL query statement below
select id, 'Root' as type
from Tree
where p_id is null
union
select id, 'Inner' as type
from Tree
where p_id is not null and id in (select p_id from Tree)
union
select id, 'Leaf' as type
from Tree
where p_id is not null and id not in (select distinct p_id from Tree where p_id is not null)
# select distinct p_id from Tree where p_id is not null