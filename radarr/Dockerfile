FROM mono:5.0
LABEL maintainer "Nicole Renée Hubbard <nicole@nicolerenee.io>"

ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} app && useradd -u ${UID} -g ${GID} app \
&& apt-get update \
&& apt-get install -y mediainfo \
&& apt-get clean

ARG TINI_VERSION=v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static /tini

RUN chmod +x /tini \
&& mkdir /radarr \
&& mkdir /config \
&& chown app:app /config

ARG RADARR_VERSION=0.2.0.1067
RUN sh -c "curl -L https://github.com/Radarr/Radarr/releases/download/v${RADARR_VERSION}/Radarr.develop.${RADARR_VERSION}.linux.tar.gz | tar zx  -C /radarr --strip-components 1"
RUN find /radarr -type d -exec chmod 0755 {} \; \
 && find /radarr -type f -exec chmod 0644 {} \;

USER app
VOLUME /config
EXPOSE 7878

ENTRYPOINT ["/tini", "--"]
CMD ["mono", "/radarr/Radarr.exe", "--no-browser", "-data=/config"]
