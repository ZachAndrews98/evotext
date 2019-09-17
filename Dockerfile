FROM alpine

RUN set -ex && echo "Installing packages..." && apk update \
    && apk add --no-cache bash python3 \
    && rm -rf /var/cache/apk/* \
