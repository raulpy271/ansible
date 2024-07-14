FROM python:3.12-alpine3.19

RUN apk add --update --no-cache openssh sshpass

RUN pip install ansible-core

COPY ansible.cfg /etc/ansible/ansible.cfg
COPY hosts /etc/ansible/hosts

