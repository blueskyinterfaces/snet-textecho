#!/bin/sh

if [ -z "$1" ]
  then
    echo "Invalid PAYMENT_ADDRESS: ./publishAndStartService.sh PAYMENT_ADDRESS"
    exit 1
fi

echo "Publishing your service. Please wait..."

TMP_FILE=/tmp/snet_Service_publish_log.txt
rm -f $TMP_FILE
snet service metadata-init service_spec textecho $1
snet service metadata-set-fixed-price 0.00000001
snet service metadata-add-endpoints http://localhost:7000
snet service publish BSI textecho -y 2>&1 | tee $TMP_FILE
python3 server.py &
snetd --config daemonConfigFile.json &
sleep 3
