import sqlite3
conn_t=sqlite3.connect("test.db")
print("compelet")
print("----------")
c=conn_t.cursor()
sql='''
create table student
(
    id int primary key not null,
    name text not null,
    age int not null,
    address text not null,
    salary int not null
);
'''
sql1='''
insert into student(
    id,name,age,address,salary)
values(1,'ql',19,"shanghai",15000);
'''
c.execute(sql1)
conn_t.commit()
conn_t.close()