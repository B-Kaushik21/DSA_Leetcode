select e2.unique_id,e1.name 
from EmployeeUNI e2 right join  Employees e1 
on e1.id=e2.id;