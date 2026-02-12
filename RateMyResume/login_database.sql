CREATE DATABASE login;
use login;
Create table logininfo(
	name varchar(50),
    email varchar(50) NOT NULL,
    password varchar(50)
);

select * from logininfo