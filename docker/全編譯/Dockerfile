FROM ubuntu:16.04 as te2
MAINTAINER sih4sing5hong5

RUN apt-get update -qq && \
  apt-get install -y locales \
    python3 python3-pip g++ python3-dev \ 
    libxslt1-dev git subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev libgoogle-perftools-dev libxmlrpc-c++.*-dev make \
    csh libc6-dev-i386 linux-libc-dev gcc-multilib libx11-dev # libx11-dev:i386

RUN locale-gen zh_TW.UTF-8
ENV LANG zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN pip3 install --upgrade pip tai5-uan5_gian5-gi2_kang1-ku7


#安裝HTS語音辨識程式.安裝htk(); \
#

RUN echo 'from 臺灣言語工具.語音合成.HTS工具.安裝HTS語音辨識程式 import 安裝HTS語音辨識程式; \
    安裝HTS語音辨識程式.安裝sptk(); \
    安裝HTS語音辨識程式.安裝hts(); \
    安裝HTS語音辨識程式.掠htsDemoScript(); \
    from 臺灣言語工具.翻譯.摩西工具.安裝摩西翻譯佮相關程式 import 安裝摩西翻譯佮相關程式; \
    安裝摩西翻譯佮相關程式.安裝gizapp();' | python3

COPY --from=sih4sing5hong5/mosesdecoder:docker /usr/local/mosesserver /usr/local/lib/python3.5/dist-packages/外部程式/mosesdecoder
