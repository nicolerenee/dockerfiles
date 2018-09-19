FROM python:2-alpine
LABEL maintainer "Nicole Renée Hubbard <nicole@nicolerenee.io>"

ARG release_name
ARG version
ARG version_numeric

ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US.UTF-8"
ENV TERM "xterm"

RUN apk add --no-cache \
    bash \
    ca-certificates \
    p7zip \
    unrar \
    --repository https://dl-4.alpinelinux.org/alpine/edge/testing

RUN wget https://github.com/nzbget/nzbget/releases/download/${version}/nzbget-${release_name}-bin-linux.run -O /tmp/nzbget.run \
 && bash /tmp/nzbget.run --destdir /opt/nzbget \
 && mkdir /config \
 && cp /opt/nzbget/nzbget.conf /config/nzbget.conf \
 && rm -rf /tmp/*

RUN addgroup -g 1000 -S nzbget \
  && adduser -u 1000 -SHG nzbget nzbget \
  && chown -R nzbget:nzbget /config /opt/nzbget

USER nzbget

ENTRYPOINT [ "/opt/nzbget/nzbget" ]
CMD [ "-s", "-o", "OutputMode=loggable", "-c", "/config/nzbget.conf" ]
