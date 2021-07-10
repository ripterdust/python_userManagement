CREATE DATABASE travels;
USE travels;


CREATE TABLE IF NOT EXISTS family(
id              int(10) auto_increment,
miles           int(10),
income          int(10),
age             int(3),
kids            int(2),

CONSTRAINT pk_family PRIMARY KEY(id)
)ENGINE = Innodb;

CREATE TABLE IF NOT EXISTS usersData(
user_uid    int(10) auto_increment,
first_name  varchar(10),
last_name   varchar(10),
gender      varchar(7),
country     varchar(15),
age         int(3),

CONSTRAINT  pk_usersData PRIMARY KEY(user_uid)
) ENGINE = Innodb;

-- insertando datos en la tabla familu
LOAD DATA INFILE 'data.csv' 
INTO TABLE family
COLUMNS TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(miles, income, age, kids);


-- Insertando datos en la tabla usersData
LOAD DATA INFILE 'usersDataCSV.csv'
INTO TABLE usersData
COLUMNS TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(first_name, last_name, gender, country, age);

'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads'


-- Consulta usersData

SELECT * FROM usersData
WHERE(
gender = 'Male' and 
country = 'France' and
age > 18 and
age < 50 and
last_name != 'Unknow' and
first_name != 'Unknow' and
first_name != 'Angel' and
first_name != 'Lester'
);

-- Obtener todos los países
SELECT country FROM usersData GROUP BY country;

-- Obtener todos los nombres
SELECT first_name, last_name FROM usersData GROUP BY first_name, last_name;
