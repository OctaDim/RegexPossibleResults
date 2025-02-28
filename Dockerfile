FROM ubuntu:latest
LABEL authors="dexp"

ENTRYPOINT ["top", "-b"]
