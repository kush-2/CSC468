# Use an official MySQL runtime as a parent image
FROM mysql/mysql-server:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD password

# Set up another MySQL user
ENV MYSQL_USER kush
ENV MYSQL_PASSWORD password

# Set up a database called csc468
ENV MYSQL_DATABASE csc468

# COPY the CSV file cattle.csv into container
COPY ./cattle.csv /Users/kush/Desktop/csc468

# COPY the SQL file maketable.sql into container
COPY ./maketable.sql /Users/kush/Desktop/csc468

# COPY the MySQL custom config to enable local_infile
COPY ./my.cnf /etc/mysql/conf.d/

# Grant necessary privileges to user
RUN echo "GRANT ALL PRIVILEGES ON csc468.* TO 'kush'@'%' WITH GRANT OPTION;" > /docker-entrypoint-initdb.d/grant_permissions.sql