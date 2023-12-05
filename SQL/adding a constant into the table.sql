select
case when id % 2 = 0 then id - 1
when (id % 2 = 1) and id != (select count(*) from Seat) then id + 1      ----(select count(*) from Seat)
else id
end as id,
student
from Seat
order by id
-------------------- for each record, we have to calculate: (select count(*) from Seat)
----Can we do better?
---Approach: using join which only calculate the count once.
select
case when id % 2 = 0 then id - 1
when (id % 2 = 1) and id != counts then id + 1
else id
end as id,
student
from Seat,
(select count(*) as counts from Seat) as seat_counts
order by id