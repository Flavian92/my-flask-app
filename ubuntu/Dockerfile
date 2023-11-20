FROM ubuntu:14.04

RUN apt-get update -y && apt-get upgrade -y && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* 

WORKDIR /ubuntuapp


CMD ["bash"]
