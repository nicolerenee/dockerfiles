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

RUN groupadd -g 1000 sonarr && useradd -u 1000 -g 1000 sonarr \
 && mkdir -p /opt/sonarr /config \
 && curl -Lo /tmp/sonarr.tar.gz "http://download.sonarr.tv/v2/master/mono/NzbDrone.master.${version_numeric}.mono.tar.gz" \
 && tar -xzvf /tmp/sonarr.tar.gz -C /opt/sonarr --strip-components 1 \
 && rm -rf /tmp/sonarr.tar.gz

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Change ownership and make sure everyone can access files
RUN chown -R sonarr:sonarr /opt/sonarr /config \
 && find /opt/sonarr -type f -print0 | xargs -0 chmod 0644

WORKDIR /opt/sonarr

USER sonarr

ENTRYPOINT ["entrypoint.sh"]
