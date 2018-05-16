FROM alpine:latest
LABEL maintainer "Nicole Renée Hubbard <nicole@nicolerenee.io>"

RUN apk add --no-cache \
    curl \
    p7zip \
    python2 \
    unrar \
    wget

ARG NZBGET_VERSION="20.0-r2181"
ARG NZBGET_BINARY_VERSION="20.0-testing-r2181"
RUN curl -L -o /tmp/nzbget.run \
      https://github.com/nzbget/nzbget/releases/download/v${NZBGET_VERSION}/nzbget-${NZBGET_BINARY_VERSION}-bin-linux.run \
 && mkdir /app /config \
 && sh /tmp/nzbget.run --destdir /app \
 && cp /app/nzbget.conf /config/nzbget.conf \
 && rm -rf /tmp/*

EXPOSE 6789

ENTRYPOINT [ "/app/nzbget" ]
CMD [ "-s", "-o", "OutputMode=log", "-c", "/config/nzbget.conf" ]
