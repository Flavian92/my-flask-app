# my-flask-app

docker push flavian92/my-flask-app:tagname
https://hub.docker.com/repository/docker/flavian92/my-flask-app/general


create appy.py
create requirements.txt
run on terminal 
pip install psutil
update repo github
run pip install -r requirements.txt
python3 app.py
on chrome run on search bar localhost:5000
![Alt text](<Screenshot from 2023-11-30 11-46-16-1.png>)
ctrl+c to stop app


Dockerise app
create docker file copy the file and the content
run docker build -t my-flask-app .
docker images to see if is created
my-flask-app                  latest          9e6defb32506   2 minutes ago   1.09GB

run docker container
docker run -p 5000:5000 9e6defb32506 
on chrome run on search bar localhost:5000

create ecr.py
run python3 ecr.py