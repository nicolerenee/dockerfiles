FROM alpine:latest

RUN apk --no-cache add nfs-utils

ADD https://github.com/ContainX/docker-volume-netshare/releases/download/v0.18/docker-volume-netshare_0.18_linux_amd64-bin /docker-volume-netshare


ENTRYPOINT ["/bin/docker-volume-netshare"]
CMD ["nfs"]
