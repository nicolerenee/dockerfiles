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
&& mkdir /sonarr \
&& mkdir /config \
&& chown app:app /config

ARG SONARR_VERSION=2.0.0.5163
RUN sh -c "curl http://download.sonarr.tv/v2/master/mono/NzbDrone.master.${SONARR_VERSION}.mono.tar.gz | tar zx  -C /sonarr --strip-components 1"

USER app
VOLUME /config
EXPOSE 8989

ENTRYPOINT ["/tini", "--"]
CMD ["mono", "/sonarr/NzbDrone.exe", "--no-browser", "-data=/config"]
