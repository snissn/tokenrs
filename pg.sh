sudo apt-get install wget ca-certificates -y
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install postgresql-11 python3-postgresql -y
sudo /etc/init.d/postgresql start


sudo pip3 install psycopg2
 echo "local   all             $USER                                peer" | sudo tee -a /etc/postgresql/11/main/pg_hba.conf
