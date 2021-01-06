set -eux

sudo apt-get install wget ca-certificates python3-pip libpq-dev python-is-python3 ipython3 -y



#https://www.postgresql.org/download/linux/ubuntu/


wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install postgresql-12 python3-postgresql -y
sudo /etc/init.d/postgresql start


sudo pip3 install psycopg2 
sudo pip3 install sqlalchemy 
sudo pip3 install web3 



 echo "local   all             $USER                                peer" | sudo tee -a /etc/postgresql/12/main/pg_hba.conf



