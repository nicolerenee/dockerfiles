FROM mono:5
LABEL maintainer "Nicole Renée Hubbard <nicole@nicolerenee.io>"

ARG release_name
ARG version
ARG version_numeric

ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US.UTF-8"
ENV TERM "xterm"

RUN apt-get update \
 && apt-get install -y mediainfo\
 && apt-get clean

RUN groupadd -g 1000 radarr && useradd -u 1000 -g 1000 radarr \
 && mkdir -p /opt/radarr /config \
 && curl -Lo /tmp/radarr.tar.gz "https://github.com/Radarr/Radarr/releases/download/${version}/Radarr.develop.${version_numeric}.linux.tar.gz" \
 && tar -xzvf /tmp/radarr.tar.gz -C /opt/radarr --strip-components 1 \
 && rm -rf /tmp/radarr.tar.gz

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Change ownership and make sure everyone can access files
RUN chown -R radarr:radarr /opt/radarr /config \
 && find /opt/radarr -type f -print0 | xargs -0 chmod 0644

WORKDIR /opt/radarr

USER radarr

ENTRYPOINT ["entrypoint.sh"]
