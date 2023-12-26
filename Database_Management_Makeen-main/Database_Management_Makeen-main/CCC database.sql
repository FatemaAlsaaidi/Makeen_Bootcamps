
-- SECTION B - 4 -(a)
CREATE TABLE college (col_code varchar(3) Not Null,
                       col_name varchar(30) NOT NULL,
                       col_location varchar(20),
					   col_contact numeric(8) Not Null);

CREATE TABLE club (cl_id numeric(3) Not Null ,
                   cl_name varchar(30) Not Null,
                   cl_description varchar(50) Not Null,
				   col_code varchar(3) Not Null);

CREATE TABLE activities (ac_id numeric(6) Not Null,
                   ac_name varchar(30) Not Null,
                   ac_description varchar(50) Not Null,
				   ac_date date Not Null,
				   ac_#participation varchar(50),
				   cl_id numeric(3) Not Null);
CREATE TABLE supporters (
  sup_id numeric(6) Not Null,
  sup_name varchar(30) Not Null,
  sup_phone CHAR(8) Not Null,
  sup_type varchar(20)Not Null);

CREATE TABLE paymentFee (
  sup_id numeric(6) Not Null,
  cl_id numeric(3) Not Null,
  bay_amount numeric(10) Not Null,
  bay_date DATE Not Null);

CREATE TABLE membership (
  me_id numeric(6) Not Null,
  me_firstName varchar(20) Not Null,
  me_lastName varchar(20) Not Null,
  me_phone CHAR(8) Not Null,
  me_email varchar(20) Not Null,
  me_address varchar(20),
  me_major varchar(20) Not Null,
  col_code varchar(3) Not Null,
  cl_id numeric(3) Not Null);

 CREATE TABLE membershipCard (
  me_id numeric(6) Not Null,
  cl_id numeric(3) Not Null,
  mc_type varchar(20) Not Null,
  mc_date DATE Not Null);

-- Section B - 4 - (b)

  -- Add primary key and foreign key to College table
ALTER TABLE college ADD CONSTRAINT pk_College PRIMARY KEY (col_code);

-- Add foreign key to Club table
ALTER TABLE club ADD CONSTRAINT fk_College_Club FOREIGN KEY (col_code) REFERENCES college(col_code);

-- Add primary key and foreign key to Club table
ALTER TABLE club ADD CONSTRAINT pk_Club PRIMARY KEY (cl_id);

-- Add foreign key to Activities table
ALTER TABLE activities ADD CONSTRAINT fk_Club_Activities FOREIGN KEY (cl_id) REFERENCES club(cl_id);

-- Add primary key to Activities table
ALTER TABLE activities ADD CONSTRAINT pk_Activities PRIMARY KEY (ac_id);

-- Add primary key to Supporter table
ALTER TABLE supporters ADD CONSTRAINT pk_Supporter PRIMARY KEY (sup_id);

-- Add foreign keys to PaymentFee table
ALTER TABLE paymentFee ADD CONSTRAINT fk_Supporter_PaymentFee FOREIGN KEY (sup_id) REFERENCES supporters(sup_id);
ALTER TABLE paymentFee ADD CONSTRAINT fk_Club_PaymentFee FOREIGN KEY (cl_id) REFERENCES club(cl_id);

-- Add foreign keys to Membership table
ALTER TABLE Membership ADD CONSTRAINT fk_College_Membership FOREIGN KEY (col_code) REFERENCES College(col_code);
ALTER TABLE Membership ADD CONSTRAINT fk_Club_Membership FOREIGN KEY (cl_id) REFERENCES club(cl_id);
ALTER TABLE Membership ADD CONSTRAINT pk_Membership PRIMARY KEY (me_id);


-- Add foreign keys to MembershipCard table
ALTER TABLE MembershipCard ADD CONSTRAINT fk_Membership_MembershipCard FOREIGN KEY (me_id) REFERENCES membership(me_id);
ALTER TABLE MembershipCard ADD CONSTRAINT fk_Club_MembershipCard FOREIGN KEY (cl_id) REFERENCES club(cl_id);

-- Add primary key to MembershipCard table
ALTER TABLE MembershipCard ADD CONSTRAINT pk_MembershipCard PRIMARY KEY (me_id, cl_id);

--Section B - 4 -(c)
ALTER TABLE membership ADD secondName varchar(20);
ALTER TABLE membershipCard ADD Numberofmembership numeric(3);
--Section B - 4 -(d)
ALTER TABLE membership DROP COLUMN secondName;
select * from membership;

--Section B - 4 -(e)
ALTER TABLE membershipCard ADD CONSTRAINT nuique_membershipCard
UNIQUE (mc_type);

ALTER TABLE college
ALTER COLUMN col_location varchar(20) NOT NULL;


ALTER TABLE college
ADD CONSTRAINT col_contactt_Check
CHECK (col_contact > 70000000);

-- Section B - 5
-- Insert rows into the College table
INSERT INTO College (col_code, col_name, col_location, col_contact)
VALUES ('RC', 'Alrustaq College', 'Alrustaq',73535454);

INSERT INTO College (col_code, col_name, col_location, col_contact)
VALUES ('IC', 'IBRI College','Ibri' ,93985553);

INSERT INTO College (col_code, col_name, col_location, col_contact)
VALUES ('SC', 'Sohar College','Sohar', 75678912);
-- Insert rows into the Club table
INSERT INTO Club (cl_id, cl_name, cl_description, col_code)
VALUES (1, 'Sports Club', 'For sports enthusiasts', 'SC');

INSERT INTO Club (cl_id, cl_name, cl_description, col_code)
VALUES (2, 'Art Club', 'Explore your artistic side', 'IC');

INSERT INTO Club (cl_id, cl_name, cl_description, col_code)
VALUES (3, 'Science Club', 'Discover the wonders of science', 'RC');

INSERT INTO Club (cl_id, cl_name, cl_description, col_code)
VALUES (4, 'Art Club', 'Discover the wonders of science', 'RC');

INSERT INTO Club (cl_id, cl_name, cl_description, col_code)
VALUES (5, 'Music Club', 'Explore your artistic side', 'IC');

INSERT INTO Club (cl_id, cl_name, cl_description, col_code)
VALUES (6, 'IT Club', 'Explore your artistic side', 'IC');


-- Insert rows into the Activities table
INSERT INTO Activities (ac_id, ac_name, ac_description, ac_date, ac_#participation, cl_id)
VALUES (1, 'Football Tournament', 'Annual football competition', '2023-07-15', '50 participants', 1);

INSERT INTO Activities (ac_id, ac_name, ac_description, ac_date, ac_#participation, cl_id)
VALUES (2, 'Art Exhibition', 'Showcase of student artwork', '2023-08-20', '100 participants', 2);

INSERT INTO Activities (ac_id, ac_name, ac_description, ac_date, ac_#participation, cl_id)
VALUES (3, 'Science Fair', 'Display of scientific experiments', '2023-09-10', '75 participants', 3);

-- Insert rows into the Supporter table
INSERT INTO supporters (sup_id, sup_name, sup_phone, sup_type)
VALUES (100, 'Ahmed Almamari', 72345678, 'Individual');

INSERT INTO supporters (sup_id, sup_name, sup_phone, sup_type)
VALUES (200, 'Muna Almusalami', 98765432, 'Corporate');

INSERT INTO supporters (sup_id, sup_name, sup_phone, sup_type)
VALUES (300, 'Ali Alsaiedi', 95678912, 'Leader');

-- Insert rows into the PaymentFee table
INSERT INTO PaymentFee (sup_id, cl_id, bay_amount, bay_date)
VALUES (100, 1, 100, '2023-07-01');

INSERT INTO PaymentFee (sup_id, cl_id, bay_amount, bay_date)
VALUES (200, 2, 75, '2023-08-05');

INSERT INTO PaymentFee (sup_id, cl_id, bay_amount, bay_date)
VALUES (300, 3, 50, '2023-09-01');

-- Insert rows into the Membership table
INSERT INTO membership(me_id,me_firstName,me_lastName,me_phone, me_email,me_address ,me_major,col_code, cl_id)
VALUES (1, 'Noor', 'Almamari', 76258633,'####@gmail.com','muscat','IT','RC',1);

INSERT INTO membership(me_id,me_firstName,me_lastName,me_phone, me_email,me_address ,me_major,col_code, cl_id)
VALUES (2, 'Mona', 'Alnasri', 96258633,'####@gmail.com','Ibri','IT','IC',2);


INSERT INTO membership(me_id,me_firstName,me_lastName,me_phone, me_email,me_address ,me_major,col_code, cl_id)
VALUES (3, 'Hajeer', 'Alsaaidi', 96896863,'####@gmail.com','Sohar','IT','SC',3);

-- Insert rows into the MembershipCard table
INSERT INTO MembershipCard (me_id, cl_id, mc_type, mc_date, Numberofmembership)
VALUES (1, 1, 'Leader', '2023-07-01', 3);

INSERT INTO MembershipCard (me_id, cl_id, mc_type, mc_date, Numberofmembership )
VALUES (2, 2, 'subervising', '2023-08-05', 5);

INSERT INTO MembershipCard (me_id, cl_id, mc_type, mc_date, Numberofmembership)
VALUES (3, 3, 'S_leader', '2023-09-01', 7);


--Section C - 6 - a
SELECT * FROM activities;
SELECT * FROM club;
SELECT * FROM college;
SELECT * FROM membership;
SELECT * FROM membershipCard;
SELECT * FROM paymentFee;
SELECT * FROM supporters;

--Section C - 6 - b
select me_firstName from membership where me_firstName LIKE'M%';

SELECT *FROM paymentFee WHERE bay_amount > 50;

SELECT * FROM membershipCard,college
WHERE Numberofmembership > 5
AND col_location = 'Ibri';

--Section C - 6 - c
SELECT sup_name,sup_phone,MAX(bay_amount) as max_payment
FROM supporters, paymentFee
group by sup_name,sup_phone ;

--Section C - 6 - d
SELECT membership.me_id, membership.me_firstName, membership.me_lastName, activities.ac_id, activities.ac_name
FROM membership
JOIN activities ON membership.me_id = activities.ac_id;


--Section C - 6 - e
SELECT sup_id, COUNT(bay_amount) AS TotalPayments, SUM(bay_amount) AS TotalAmount, AVG(bay_amount) AS AverageAmount
FROM paymentFee
GROUP BY sup_id;




--Section C - 6 - f
SELECT c.col_name AS CollegeName, COUNT(cl.cl_id) AS TotalClubs
FROM college c
LEFT JOIN club cl ON c.col_code = cl.col_code
GROUP BY c.col_code, c.col_name;




