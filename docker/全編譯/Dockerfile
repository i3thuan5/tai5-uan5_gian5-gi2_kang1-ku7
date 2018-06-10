FROM ubuntu:16.04 as te2
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

RUN echo 'from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式; 安裝摩西翻譯佮相關程式.安裝gizapp()' | python3
RUN echo 'from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式; 安裝摩西翻譯佮相關程式.安裝moses(編譯CPU數=2)' | python3 
