FROM ubuntu:20.04
ARG SSH_PORT=8080
ARG USER=node-user
ARG PASSWORD=node-pass

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y sudo python3-pip python3-apt openssh-server 

RUN useradd -m -s /bin/bash -Gsudo $USER
RUN echo "$USER:$PASSWORD" | chpasswd

# https://askubuntu.com/questions/1109934/ssh-server-stops-working-after-reboot-caused-by-missing-var-run-sshd/1110843#1110843
RUN mkdir -p -m0755 /var/run/sshd

EXPOSE $SSH_PORT

ENV SSH_PORT_ENV=$SSH_PORT
ENTRYPOINT /usr/sbin/sshd -D -p $SSH_PORT_ENV

