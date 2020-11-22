FROM ubuntu:20.04

COPY install-packages.sh .
RUN ./install-packages.sh
