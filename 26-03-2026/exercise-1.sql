create database company_training;
use company_training;

create table employees (
    emp_id int primary key,
    emp_name varchar(100),
    department varchar(50),
    city varchar(50)
);

create table projects (
    project_id int primary key,
    emp_id int,
    project_name varchar(100),
    project_budget decimal(12,2),
    project_status varchar(50)
);

insert into employees values
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', 'Kolkata'),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, null, 'Marketing', 'Chennai');

insert into projects values
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, null, 'HR Survey', 30000, 'Planning'),
(106, 8, 'Mobile App', 100000, 'Active');

select employees.emp_name, projects.project_name, projects.project_budget
from employees
inner join projects
on employees.emp_id = projects.emp_id;

select employees.emp_name, projects.project_name
from employees
left join projects
on employees.emp_id = projects.emp_id;

select employees.emp_name, projects.project_name
from employees
right join projects
on employees.emp_id = projects.emp_id;

select employees.emp_name, projects.project_name
from employees
left join projects
on employees.emp_id = projects.emp_id
union all
select employees.emp_name, projects.project_name
from employees
right join projects
on employees.emp_id = projects.emp_id;

select employees.emp_name, projects.project_name
from employees
cross join projects;

select employees.emp_name, projects.project_name
from employees
join projects
on employees.emp_id = projects.emp_id
where employees.department = 'IT';

select * from projects
where project_budget > 100000;

select employees.emp_name, projects.project_name
from employees
join projects
on employees.emp_id = projects.emp_id
where employees.city = 'Hyderabad';

select employees.emp_name, count(*) as total_projects
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.emp_name;

select employees.emp_name, sum(projects.project_budget) as total_budget
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.emp_name;

select employees.department, avg(projects.project_budget) as average_budget
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.department;

select employees.department, count(*) as total_projects
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.department;

select employees.department, sum(projects.project_budget) as total_dep_budget
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.department;

select city, count(*) as emp_count
from employees
group by city;

select employees.emp_name, count(*) as more_project_count
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.emp_name
having count(*) > 1;

select employees.department, sum(projects.project_budget) as total_budget_150k
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.department
having sum(projects.project_budget) > 150000;

select employees.emp_name, sum(projects.project_budget) as total_budget_100k
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.emp_name
having sum(projects.project_budget) > 100000;

select employees.emp_name, employees.department, sum(projects.project_budget) as total_budget_over_100k
from employees
join projects
on employees.emp_id = projects.emp_id
group by employees.emp_name, employees.department
having sum(projects.project_budget) > 100000
order by sum(projects.project_budget) desc;
