#!/bin/bash
if [ "$#" != "1" ];then
	echo "Usage $0 [string]"
	exit 1;
fi
cd "$(dirname "$0")"
random=`echo $RANDOM`
CKIP_INPUT="/tmp/ckip.input.$random"
CKIP_OUTPUT="/tmp/ckip.output.$random"
FileName="ckip.tmp"
rm -rf ${CKIP_INPUT}/ ${CKIP_OUTPUT}/
mkdir ${CKIP_INPUT} ${CKIP_OUTPUT}
echo $1 | iconv -f utf8 -t big5 > ${CKIP_INPUT}/${FileName}
export _JAVA_OPTIONS="-Dfile.encoding=big5"
/usr/bin/java -jar CKIPParser.jar ckipsocket.parser.propeties ${CKIP_INPUT} ${CKIP_OUTPUT} > /dev/null  2>&1
iconv -f big5 -t utf8 ${CKIP_OUTPUT}/${FileName}
rm -rf ${CKIP_INPUT}/ ${CKIP_OUTPUT}/
exit 0
