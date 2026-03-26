create database capstone_sql;
use capstone_sql;

create table students (
    student_id int primary key,
    student_name varchar(100),
    city varchar(50),
    age int
);

create table enrollments (
    enrollment_id int primary key,
    student_id int,
    course_name varchar(100),
    trainer varchar(100),
    fee decimal(10,2)
);

insert into students values
(1, 'Aarav Sharma', 'Hyderabad', 22),
(2, 'Priya Reddy', 'Bangalore', 23),
(3, 'Rahul Verma', 'Mumbai', 24),
(4, 'Sneha Kapoor', null, 21),
(5, 'Vikram Singh', 'Chennai', 25),
(6, null, 'Delhi', 22);

insert into enrollments values
(101, 1, 'MySQL', 'Abdullah Khan', 5000),
(102, 1, 'Python', 'Abdullah Khan', 7000),
(103, 2, 'Power BI', 'Kiran', 6000),
(104, 3, 'Azure Data Factory', 'Sneha', 8000),
(105, null, 'Excel', 'Rohan', 3000),
(106, 8, 'Databricks', 'Ananya', 9000);

select students.student_name, enrollments.course_name
from students
inner join enrollments
on students.student_id = enrollments.student_id;

select students.student_name, enrollments.course_name
from students
left join enrollments
on students.student_id = enrollments.student_id;

select students.student_name, enrollments.course_name
from students
right join enrollments
on students.student_id = enrollments.student_id;

select students.student_name, enrollments.course_name
from students
left join enrollments
on students.student_id = enrollments.student_id
union all
select students.student_name, enrollments.course_name
from students
right join enrollments
on students.student_id = enrollments.student_id
where students.student_id is null;

select students.student_name, enrollments.course_name
from students
cross join enrollments;

select students.student_name, enrollments.course_name
from students
join enrollments
on students.student_id = enrollments.student_id
where students.city = 'Hyderabad';

select *
from enrollments
where fee > 6000;

select students.student_name, count(enrollments.course_name)
from students
join enrollments
on students.student_id = enrollments.student_id
group by students.student_id, students.student_name;

select students.student_name, sum(enrollments.fee)
from students
join enrollments
on students.student_id = enrollments.student_id
group by students.student_id, students.student_name;

select students.student_name, count(enrollments.course_name)
from students
join enrollments
on students.student_id = enrollments.student_id
group by students.student_id, students.student_name
having count(enrollments.course_name) > 1;

select enrollments.trainer, sum(enrollments.fee)
from enrollments
group by enrollments.trainer
having sum(enrollments.fee) > 10000;

select city, count(student_id)
from students
group by city
having count(student_id) > 1;

select students.student_name, students.city, sum(enrollments.fee) as total_fee_over_5k
from students
join enrollments
on students.student_id = enrollments.student_id
group by students.student_name, students.city
having sum(enrollments.fee) > 5000
order by sum(enrollments.fee) desc;
