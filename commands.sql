
###POSTGRES

#entering db
sudo -u postgres psql

#runing sql files
sudo -u postgres psql -f create_table.sql

#copy table
sudo -u postgres psql -c "\COPY dsu.dsu FROM 'traffic.csv' DELIMITER ';' CSV";



###MySQL 
#entering db
mysql -u root -p -h localhost
(next will be propmt the pass)

#runing sql files
mysql -u root -p -h localhost < create_table.sql


#for creating the table, you must select the db (use db_name)
#example:
mysql> CREATE TABLE dsu(
 Start_Time                  VARCHAR(26) 
,End_Time                    VARCHAR(26) );


#copy csv to tables
mysql -u root -p -h localhost < populate.sql


