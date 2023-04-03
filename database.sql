create database tmcjamroom;
use tmcjamroom;
create table members (reg_no int not null, fname varchar(25) not null, lname varchar(25) not null, field 
varchar(25) not null, residence varchar(25) not null, sex char(1) not null);
alter table members add primary key(reg_no);
create table schedule(slot_id varchar(25) not null, firstname varchar(25) , lastname varchar(25) , 
start_time varchar(25) not null, end_time varchar(25) not null, status varchar(25) not null, day 
varchar(25) not null);
insert into schedule(slot_id,start_time, end_time, status,day)values('1','5','6','Available','null');
insert into schedule(slot_id,start_time, end_time, status,day)values('2','6','7','Available','null');
insert into schedule(slot_id,start_time, end_time, status,day)values('3','7','8','Available','null');
insert into schedule(slot_id,start_time, end_time, status,day)values('4','8','9','Available','null');
insert into schedule(slot_id,start_time, end_time, status,day)values('5','9','10','Available','null');
insert into schedule(slot_id,start_time, end_time, status,day)values('6','10','11','Available','null');
alter table schedule add primary key(slot_id);
alter table schedule add foreign key(slot_id) references members(reg_no);
create table viewins(slot_id int(11) not null, firstname varchar(25), reg_no int(25), start_time 
varchar(25) not null, end_time varchar(25) not null, inst_used varchar(100));
insert into viewins(slot_id, start_time, end_time)values(1,'5','6');
insert into viewins(slot_id, start_time, end_time)values(2,'6','7');
insert into viewins(slot_id, start_time, end_time)values(3,'7','8');
insert into viewins(slot_id, start_time, end_time)values(4,'8','9');
insert into viewins(slot_id, start_time, end_time)values(5,'9','10');
insert into viewins(slot_id, start_time, end_time)values(6,'10','11');
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`) values(169105142, 
“Rashi”, “Singh”, “Vocalist”, “Hosteler”, “f”);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169105150, 
“Ritwik”, “Srivastava”, “Guitarist”, “Hosteler”, “m”);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169105056, 
‘Avantika’, ‘Sharma’, ‘Vocalist’, ‘Hosteler’, ‘f’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169105142, 
‘Poojitha’, ‘Konduparthi’, ‘Vocalist’, ‘Hosteler’, ‘f’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159108084, ‘Parth’, 
‘Saraswat’, ‘Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159102041, 
‘Garvit’, ‘Kumar’, ‘Drummer’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169105085, ‘Ishan’, 
‘Rawat’, ‘Vocalist’, ‘Day Scholar’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169105131, ‘Prerit’, 
‘Pathak’, ‘Vocalist/Instrumentalist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169108042, 
‘Christy’, ‘Isadore’, ‘Guitarist/Vocalist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169110013, 
‘Atharv’, ‘Dixit’, ‘Vocalist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169108024, 
‘Ankita’, ‘Tuli’, ‘Vocalist’, ‘Hosteler’, ‘f’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(179403015, 
‘Bhavnitt’, ‘Singh’, ‘Keyboardist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(179303085, 
‘Mehul’, ‘Gupta’, ‘Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(179302035, 
‘Atharv’, ‘Sinha’, ‘Vocalist/Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(161401032, 
‘Gayathri’, ‘Nair’, ‘Vocalist’, ‘Hosteler’, ‘f’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159106049, 
‘Bhavya’, ‘Bhatia’, ‘Vocalist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159101128, 
‘Shaurya’, ‘Mathur’, ‘Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159108078, 
‘Nishant’, ‘Seth’, ‘Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159101103, 
‘Raghav’, ‘Kaul’, ‘Keyboardist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159103086, 
‘Naman’, ‘Kumar’, ‘Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(179102050, 
‘Utkarsh’, ‘Jain’, ‘Drummer’, ‘Day Scholar’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(171102010, ‘Rhea’, 
‘Sharma’, ‘Vocalist’, ‘Hosteler’, ‘f’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169107006, 
‘Abhyudya’, ‘Bhatnagar’, ‘Vocalist/Guitarist’, ‘Day Scholar’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159101134, 
‘Shourojit’, ‘Dutt’, ‘Drummer’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159102026, 
‘Arunima’, ‘Mishra’, ‘Vocalist’, ‘Hosteler’, ‘f’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169109003, ‘Aatif’, 
‘Ahmad’,’Guitarist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159103081, 
‘Pranav’, ‘Sehgal’, ‘Guitarist’, ‘Day Scholar’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(159101006, 
‘Abhimanyu’, ‘Kaul’, ‘Vocalist’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(179202100, ‘Rahul’, 
‘Roy’, ‘Drummer’, ‘Hosteler’, ‘m’);
INSERT INTO `members` (`reg_no`, `fname`, `lname`, `field`, `residence`, `sex`)values(169107176, 
‘Tanay’, ‘Nambiar’, ‘Vocalist’, ‘Hosteler’, ‘m’);
insert INTO schedule(slot_id,start_time,end_time, status) values('1','5','6','Available');
insert INTO schedule(slot_id,start_time,end_time, status) values('2','6','7','Available');
insert INTO schedule(slot_id,start_time,end_time, status) values('3','7','8','Available');
insert INTO schedule(slot_id,start_time,end_time, status) values('4','8','9','Available');
insert INTO schedule(slot_id,start_time,end_time, status) values('5','9','10','Available');
insert INTO schedule(slot_id,start_time,end_time, status) values('6','10','11','Available');
create table admin(reg_no varchar(25) not null, fname varchar(25) not null, lname varchar(25) not null);
insert into admin(reg_no, fname,lname) VALUES('169105142','Rashi','Singh');
insert into admin(reg_no, fname,lname) VALUES('169105056','Avantika','Sharma');
insert into admin(reg_no, fname,lname) VALUES('169105085','Ishan','Rawat');
insert into admin(reg_no, fname,lname) VALUES('169105142','Tanay','Nambiar');
create table equipment(inst_id int not null, inst_name varchar(25) not null, inst_checked varchar(25) 
not null);
insert into equipment(inst_id, inst_name) values(1,'Drums');
insert into equipment(inst_id, inst_name) values(2,'Acoustic Guitar');
insert into equipment(inst_id, inst_name) values(3,'Electric Guitar');
insert into equipment(inst_id, inst_name) values(4,'Bass Guitar');
insert into equipment(inst_id, inst_name) values(5,'Cajon');
insert into equipment(inst_id, inst_name) values(6,'Tabla');
insert into equipment(inst_id, inst_name) values(7,'Amps');
insert into equipment(inst_id, inst_name) values(8,'Microphone');
insert into equipment(inst_id, inst_name) values(9,'Keyboard')
