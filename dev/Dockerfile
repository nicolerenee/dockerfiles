FROM ubuntu:latest
LABEL maintainer "Nicole Renée Hubbard <nicole@nicolerenee.io>"

ENV SSH_USER "nicole"
ENV GITHUB_USER "nicolerenee"
ENV SHELL "/bin/bash"

RUN apt-get update \
 && apt-get upgrade -y --no-install-recommends \
 && apt-get install -y --no-install-recommends \
  bash \
  ca-certificates \
  curl \
  git-core \
  htop \
  jq \
  locales \
  man \
  net-tools \
  netcat \
  openssh-client \
  openssh-server \
  rsync \
  sudo \
  unzip \
  vim \
  wget \
  zip \
  zsh \
 && mkdir /var/run/sshd \
 && locale-gen en_US.UTF-8

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config \
 && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \
 && sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

EXPOSE 22

ENTRYPOINT ["entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
