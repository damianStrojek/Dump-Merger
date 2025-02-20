create database my_database;
show databases;
use my_database;
drop table Merge;

CREATE TABLE `my_database`.`merge` (
  `source` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `date` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `username` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `email` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `password` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL,
  `hash` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

SELECT COUNT(*) FROM merge;

SET GLOBAL local_infile=1;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\1.5M POLAND GOOD QUALITY COMBOLIST.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\1500000_data_random_websites.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\3.5mlnPLmailpass.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\dump-agusiq-torrents.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\bp-blogplay-users-dump.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\cdprojectred.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\daniel_hosting.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Electroworld.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\inpost.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Ledger.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\pl2023_dump.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\forum-torepublic.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\wakacje_pl_forum_dump.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\zapiszjako.pl_poczatek2016.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Badoo.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\sample.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\tiktok_com_logpass.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\westernunion_com.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\BitcoinTalk-org.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\vbuser_forumplay.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\kssipgovpl.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\morele-users.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY "'"           -- Values enclosed in quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\DB_Noclegi.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\sellaccs247.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\24_5_mln_emaile_i_passy.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row


LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\CANVA_FULL_CLEANED-1.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\CANVA_FULL_CLEANED-2.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

select COUNT(*) from merge;

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\DehashedDatabase-1.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\DehashedDatabase-2.csv'
INTO TABLE merge
FIELDS TERMINATED BY ','  -- Field separator (comma for CSV)
ENCLOSED BY '"'           -- Values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Line separator (use '\r\n' for Windows-style line endings)
IGNORE 1 ROWS;           -- Skip the header row

select * from merge;

SELECT * FROM my_database.merge
WHERE password LIKE '%password%';


