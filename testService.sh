#!/bin/bash

# Usage: testService.sh A
#
# A is a text string
#
# Prints echo of A

if [ -z "$1" ]
  then
    echo "Invalid ARGUMENTS: ./testServiceRequest.sh VALUE_A"
    exit 1
fi

snet client deposit 0.00000001 -y
snet client open_init_channel_registry BSI textecho 0.00000001 11000000 -y
snet client call 0 0.00000001 localhost:7000 echo "{\"in_text\":$1}"
