USE csc468;

CREATE TABLE cattle(
	id INT AUTO_INCREMENT PRIMARY TAG,
	name VARCHAR(255) NOT NULL,
	color VARCHAR(255)
);

load data infile '/Users/kush/Desktop/csc468/cattle.csv'
into table cattle
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;
