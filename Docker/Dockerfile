FROM ubuntu:18.04

ARG language

ENV SINGNET_REPOS=/opt/singnet
ENV GOPATH=${SINGNET_REPOS}/go
ENV PATH=${GOPATH}/bin:${PATH}

RUN mkdir -p ${GOPATH}

RUN apt-get update && \
    apt-get install -y \
    apt-utils \
    nano \
    git \
    wget \
    curl \
    zip \
    libudev-dev \
    libusb-1.0-0-dev

RUN apt-get install -y nodejs npm
RUN apt-get install -y python3 python3-pip

RUN cd ${SINGNET_REPOS} && \
    git clone https://github.com/singnet/snet-cli && \
    cd snet-cli && \
    ./scripts/blockchain install && \
    pip3 install -e .

RUN cd ${SINGNET_REPOS} && \
    mkdir snet-daemon && \
    cd snet-daemon && \
    wget https://github.com/singnet/snet-daemon/releases/download/v0.1.3/snetd-0.1.3.tar.gz && \
    tar -xvf snetd-0.1.3.tar.gz && \
    mv ./linux-amd64/snetd /usr/bin/snetd

RUN cd ${SINGNET_REPOS} && \
    git clone https://github.com/blueskyinterfaces/snet-textecho.git && \
    cd snet-textecho && \
    chmod 755 buildProto.sh && \
    chmod 755 publishAndStartService.sh && \
    chmod 755 testService.sh
 
WORKDIR ${SINGNET_REPOS}
