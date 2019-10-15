#!/bin/bash
set -e

PASSWD=`openssl rand -base64 32`
ENC_PASSWD=`openssl passwd -1 -salt xyz $PASSWD`
useradd -m -u 1000 -p '$ENC_PASSWD' -s /bin/bash $SSH_USER
mkdir -p /home/$SSH_USER/.ssh
wget https://github.com/${GITHUB_USER}.keys -O /home/$SSH_USER/.ssh/authorized_keys
chown -R $SSH_USER:$SSH_USER /home/$SSH_USER/.ssh
chmod 700 /home/$SSH_USER/.ssh
chmod 600 /home/$SSH_USER/.ssh/authorized_keys

exec "$@"
