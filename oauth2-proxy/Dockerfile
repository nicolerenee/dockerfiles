FROM alpine:3.6

RUN addgroup oauth2_proxy && adduser -G oauth2_proxy -D -H oauth2_proxy

ARG OAUTH2_PROXY_RELEASE_VER=2.2
ARG OAUTH2_PROXY_VERSION=2.2.0

RUN set -xe \
    && apk add --no-cache --virtual .run-deps \
        bash \
        ca-certificates \
        curl \
    && apk add --no-cache --virtual .build-deps \
        tar \
    && mkdir /oauth2_proxy \
    && curl -O -fSL "https://github.com/bitly/oauth2_proxy/releases/download/v${OAUTH2_PROXY_RELEASE_VER}/oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-amd64.go1.8.1.tar.gz" \
    && tar -xf oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-amd64.go1.8.1.tar.gz -C /oauth2_proxy --strip-components=1 --no-same-owner \
    && rm oauth2_proxy-${OAUTH2_PROXY_VERSION}.linux-amd64.go1.8.1.tar.gz \
    && mkdir /conf /templates \
    && chown -R oauth2_proxy:oauth2_proxy /conf /templates /oauth2_proxy \
    && apk del .build-deps

VOLUME /config
VOLUME /templates

LISTEN 4180

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
    CMD curl --silent --fail http://localhost:4180/ping || exit 1

ENTRYPOINT [ "/oauth2_proxy/oauth2_proxy" ]
CMD [ "--config", "/conf/oauth2_proxy.cfg" ]
