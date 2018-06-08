FROM ubuntu:16.04
MAINTAINER sih4sing5hong5

RUN apt-get update -qq && \
  apt-get install -y locales \
    python3 python3-pip g++ python3-dev \ 
    libxslt1-dev git subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev libgoogle-perftools-dev libxmlrpc-c++.*-dev make \
    csh libc6-dev-i386 linux-libc-dev gcc-multilib libx11-dev # libx11-dev:i386

RUN pip3 install --upgrade pip

RUN locale-gen zh_TW.UTF-8
ENV LANG zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN pip3 install tai5-uan5_gian5-gi2_kang1-ku7

RUN echo 'from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式; 安裝KenLM訓練程式.安裝kenlm()' | python3
COPY --from=sih4sing5hong5/mosesdecoder:docker /usr/local/mosesserver/bin/mosesserver /usr/local/lib/python3.5/dist-packages/外部程式/mosesdecoder/bin/mosesserver
