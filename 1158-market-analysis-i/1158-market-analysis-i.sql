# Write your MySQL query statement below
select user_id as buyer_id, join_date, count(Orders.buyer_id) as orders_in_2019
from Users left join Orders on Users.user_id=Orders.buyer_id and order_date like '2019%'
group by user_id