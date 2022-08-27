# Write your MySQL query statement below
select name, ifnull(sum(Rides.distance), 0) as 'travelled_distance'
from Users left join Rides on Rides.user_id=Users.id
group by user_id
order by travelled_distance desc, name asc