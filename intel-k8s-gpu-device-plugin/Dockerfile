# Original at https://github.com/intel/intel-device-plugins-for-kubernetes/blob/master/build/docker/intel-gpu-plugin.Dockerfile
FROM golang:1.10-alpine as builder
ARG VERSION
ARG DIR=/go/src/github.com/intel/intel-device-plugins-for-kubernetes
RUN apk add --no-cache \
		git
RUN git clone https://github.com/intel/intel-device-plugins-for-kubernetes.git $DIR
WORKDIR $DIR
RUN git checkout $VERSION
RUN cd cmd/gpu_plugin; go install
RUN chmod a+x /go/bin/gpu_plugin

FROM alpine
COPY --from=builder /go/bin/gpu_plugin /usr/bin/intel_gpu_device_plugin
CMD ["/usr/bin/intel_gpu_device_plugin"]
