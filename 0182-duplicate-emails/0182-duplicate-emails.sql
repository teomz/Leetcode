
select p1.email
from 
person p1
left join
person p2
using(email)
where p1.id > p2.id
group by 1