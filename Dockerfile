FROM python:3.7-stretch
MAINTAINER sih4sing5hong5

RUN pip install tai5-uan5_gian5-gi2_kang1-ku7

RUN apt-get update -qq && \
   apt-get install -y cmake libboost-all-dev
RUN echo 'from 臺灣言語工具.語言模型.安裝KenLM訓練程式 import 安裝KenLM訓練程式; 安裝KenLM訓練程式.安裝kenlm()' | python
COPY --from=sih4sing5hong5/mosesdecoder:docker /usr/local/mosesserver/bin/mosesserver /usr/local/lib/python3.7/site-packages/外部程式/mosesserver
